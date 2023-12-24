from flask  import Flask, render_template, request
# import jsonify
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model1 = pickle.load(open('Stress_Detection.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('mental.html')




@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender =request.form['gender']
        if(Gender=='Male'):
            Gender=1
        else:
            Gender=0
        Age=int(request.form['Age'])
        Blank_mind=request.form['Blank_mind']
        if(Blank_mind=='Strongly_agree'):
            Blank_mind = 3
        elif(Blank_mind=='Agree'):
            Blank_mind = 0
        elif(Blank_mind=='Neutral'):
            Blank_mind = 2
        elif(Blank_mind=='Disagree'):
            Blank_mind = 1
        else:
            Blank_mind =4
        Anxiety_works =request.form['Anxiety_works']
        if(Anxiety_works=='Strongly_agree'):
            Anxiety_works = 3
        elif(Anxiety_works=='Agree'):
            Anxiety_works = 0
        elif(Anxiety_works=='Neutral'):
            Anxiety_works = 2
        elif(Anxiety_works=='Disagree'):
            Anxiety_works = 1
        else:
            Anxiety_works = 4
        Anxiety_social_life=request.form['Anxiety_social']
        if(Anxiety_social_life=='Strongly_agree'):
            Anxiety_social_life = 3
        elif(Anxiety_social_life=='Agree'):
            Anxiety_social_life = 0
        elif(Anxiety_social_life=='Neutral'):
            Anxiety_social_life = 2
        elif(Anxiety_social_life=='Disagree'):
            Anxiety_social_life = 1
        else:
            Anxiety_social_life = 4
        Anxiety_presonal=request.form['Anxiety_personal']
        if(Anxiety_presonal=='Strongly_agree'):
            Anxiety_presonal = 3
        elif(Anxiety_presonal=='Agree'):
            Anxiety_presonal = 0
        elif(Anxiety_presonal=='Neutral'):
            Anxiety_presonal = 2
        elif(Anxiety_presonal=='Disagree'):
            Anxiety_presonal = 1
        else:
            Anxiety_presonal = 4
        Attention_class=request.form['Attention_class']
        if(Attention_class=='Strongly_agree'):
            Attention_class = 3
        elif(Attention_class=='Agree'):
            Attention_class = 0
        elif(Attention_class=='Neutral'):
            Attention_class = 2
        elif(Attention_class=='Disagree'):
            Attention_class = 1
        else:
            Attention_class = 4
        time=request.form['time']
        if(time=='hr1'):
            time = 0
        elif(time=='hr2'):
            time = 1
        elif(time=='hr3'):
            time = 2
        elif(time=='hr4'):
            time = 3
        else:
            time = 4
        struggle_goals=request.form['goals']
        if(struggle_goals=='Strongly_agree'):
            struggle_goals = 3
        elif(struggle_goals=='Agree'):
            struggle_goals = 0
        elif(struggle_goals=='Neutral'):
            struggle_goals = 2
        elif(struggle_goals=='Disagree'):
            struggle_goals = 1
        else:
            struggle_goals = 4
        struggle_newthings=request.form['newthings']
        if(struggle_newthings=='Strongly_agree'):
            struggle_newthings = 3
        elif(struggle_newthings=='Agree'):
            struggle_newthings = 0
        elif(struggle_newthings=='Neutral'):
            struggle_newthings = 2
        elif(struggle_newthings=='Disagree'):
            struggle_newthings = 1
        else:
            struggle_newthings = 4
        work_satisfaction=request.form['work_satisfaction']
        if(work_satisfaction=='Strongly_agree'):
            work_satisfaction = 3
        elif(work_satisfaction=='Agree'):
            work_satisfaction = 0
        elif(work_satisfaction=='Neutral'):
            work_satisfaction = 2
        elif(work_satisfaction=='Disagree'):
            work_satisfaction = 1
        else:
            work_satisfaction = 4
        Times_of_day=request.form['times_of_day']
        if(Times_of_day=='Morning'):
            Times_of_day = 1
        elif(Times_of_day=='Afternoon'):
            Times_of_day = 0
        elif(Times_of_day=='Evening'):
            Times_of_day = 2
        else:
            Times_of_day = 3
        Psycological_effects=request.form['psyco']
        if(Psycological_effects=='Anger'):
            Psycological_effects = 0
        elif(Psycological_effects=='Fear'):
            Psycological_effects = 1
        elif(Psycological_effects=='Loneliness'):
            Psycological_effects = 2
        elif(Psycological_effects=='Sadness'):
            Psycological_effects = 3
        else:
            Psycological_effects = 4 
        relieve_stress=request.form['relive']
        if(relieve_stress=='Eating'):
            relieve_stress = 0
        elif(relieve_stress=='Games'):
            relieve_stress = 1
        elif(relieve_stress=='Sleeping'):
            relieve_stress = 2
        else:
            relieve_stress = 3


        result=model1.predict([[Gender,Age,Blank_mind,Times_of_day,Anxiety_works,Anxiety_social_life,Anxiety_presonal,Attention_class,time,struggle_goals,struggle_newthings,Psycological_effects,relieve_stress,work_satisfaction]])

        if (result==0):
            return render_template('mental.html',pred="You have HIGH STRESS, Do Meditation, Get outside with others, Connect with Nature, and Explore Green spaces.")
        elif(result==1):
            return render_template('mental.html',pred="You have LOW STRESS, No need to worry Your in Normal condition")
        else:
            pred = "You have MEDIUM STRESS, Your are in better condition ,Take deep breathes, Relax some time"
            return render_template('mental.html',pred=pred)
    else:
        return render_template('mental.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

