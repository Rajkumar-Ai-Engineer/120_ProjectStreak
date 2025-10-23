from flask import Flask, render_template, request, jsonify, session
from MCQ import MCQGenerator
import json
import re
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'


quiz_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    try:
        data = request.json
        topic = data.get('topic')
        num_questions = int(data.get('num_questions', 5))
        level = data.get('level', 'easy')
        
        # Create new quiz session
        session_id = str(uuid.uuid4())
        generator = MCQGenerator()
        
        # Store session with quiz parameters
        quiz_sessions[session_id] = {
            'generator': generator,
            'topic': topic,
            'num_questions': num_questions,
            'level': level,
            'current_question': 0,
            'score': 0,
            'answers': [],
            'generated_questions': []
        }
        
        # Generate first question
        first_question = generate_single_question(session_id, 0)
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'total_questions': num_questions,
            'first_question': first_question
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get_question/<session_id>/<int:question_num>')
def get_question(session_id, question_num):
    if session_id not in quiz_sessions:
        return jsonify({'success': False, 'error': 'Session not found'})
    
    session_data = quiz_sessions[session_id]
    
    if question_num >= session_data['num_questions']:
        return jsonify({'success': False, 'error': 'Question not found'})
    
    # Generate question if not already generated
    question = generate_single_question(session_id, question_num)
    
    return jsonify({
        'success': True,
        'question': question,
        'question_number': question_num + 1,
        'total_questions': session_data['num_questions']
    })

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    try:
        data = request.json
        session_id = data.get('session_id')
        answer = data.get('answer')
        question_num = data.get('question_num')
        
        if session_id not in quiz_sessions:
            return jsonify({'success': False, 'error': 'Session not found'})
        
        session_data = quiz_sessions[session_id]
        generator = session_data['generator']
        
        # Get AI evaluation
        current_question = session_data['generated_questions'][question_num]
        evaluation = generator.answer_quiz(answer, current_question['full_text'])
        
        # Store answer
        session_data['answers'].append({
            'question_num': question_num,
            'answer': answer,
            'evaluation': evaluation
        })
        
        # Check if correct (simple parsing)
        is_correct = 'correct' in evaluation.lower() or 'right' in evaluation.lower()
        if is_correct:
            session_data['score'] += 1
        
        return jsonify({
            'success': True,
            'evaluation': evaluation,
            'is_correct': is_correct,
            'current_score': session_data['score']
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get_results/<session_id>')
def get_results(session_id):
    if session_id not in quiz_sessions:
        return jsonify({'success': False, 'error': 'Session not found'})
    
    session_data = quiz_sessions[session_id]
    
    return jsonify({
        'success': True,
        'score': session_data['score'],
        'total_questions': session_data['num_questions'],
        'answers': session_data['answers']
    })

def generate_single_question(session_id, question_num):
    """Generate a single question for the quiz"""
    session_data = quiz_sessions[session_id]
    
    # Check if question already generated
    if question_num < len(session_data['generated_questions']):
        return session_data['generated_questions'][question_num]
    
    generator = session_data['generator']
    
    # Generate single question
    quiz_text = generator.run_quiz(
        topic=session_data['topic'],
        num_questions=1,
        valuation="one_by_one",
        delivery_mode="quiz",
        level=session_data['level']
    )
    
    # Parse the single question
    question = parse_single_question(quiz_text)
    
    # Store the generated question
    session_data['generated_questions'].append(question)
    
    return question

def parse_single_question(quiz_text):
    """Parse a single question from AI response"""
    lines = quiz_text.strip().split('\n')
    question_text = ""
    options = []
    
    # Stop parsing when we hit answer/explanation section
    answer_keywords = ['answer:', 'correct answer:', 'explanation:', 'the correct answer is', 'answer is']
    
    question_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Stop if we hit answer section
        if any(keyword in line.lower() for keyword in answer_keywords):
            break
            
        # Check if it's an option
        if re.match(r'^[A-D][\.\)]', line):
            option_text = re.sub(r'^[A-D][\.\)]\s*', '', line)
            options.append(option_text)
        else:
            
            clean_line = re.sub(r'^\d+\.\s*|\*\*Question\s*\d*\*\*:?\s*|\*\*Q\d*\*\*:?\s*|topic:\s*|level:\s*|num_questions:\s*|valuation:\s*|delivery_mode:\s*|real_time_quiz_tool:\s*', '', line, flags=re.IGNORECASE)
            if clean_line and not re.match(r'^(topic|level|num_questions|valuation|delivery_mode|real_time_quiz_tool):', clean_line, re.IGNORECASE):
                question_lines.append(clean_line)
    
    
    if question_lines:
        question_text = ' '.join(question_lines)
       
        for keyword in answer_keywords:
            if keyword in question_text.lower():
                question_text = question_text[:question_text.lower().find(keyword)].strip()
                break
    
    # Clean options to remove any answer indicators
    clean_options = []
    for option in options:
        # Remove answer indicators from options
        clean_option = option
        for keyword in ['(correct)', '(answer)', '*correct*', '**correct**']:
            clean_option = clean_option.replace(keyword, '').strip()
        clean_options.append(clean_option)
    
    return {
        'text': question_text.strip() or "Question could not be parsed",
        'options': clean_options[:4] if len(clean_options) >= 4 else ["Option A", "Option B", "Option C", "Option D"],
        'full_text': quiz_text
    }

if __name__ == '__main__':
    app.run(debug=True)