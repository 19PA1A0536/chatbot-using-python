'''
This functions returns the greeting message according to the tym
'''
from datetime import datetime
import random
def current_time():
    current_time = datetime.now()
    greeting="Good morning"
    if current_time.hour>12 and current_time.hour<17:
        greeting="Good afternoon"
    elif current_time.hour>=17 and current_time.hour<22:
        greeting="Good evening"
    elif current_time.hour>=22:
        greeting="Hi, its too late"
    return greeting
'''
This function gives the welcome message
'''

def welcome(name):
    message = [
        "<==How may I help you?",
        "<==Is there anything I can help with?",
        "<==How can i help you?"
    ]
    print(f"{current_time()}!, {name}, {random.choice(message)}")

def show_opt():
    print("1. Top 10 Upcoming IT Skills")
    print("2. The 10 Skills You’ll Need By 2020")
    print("3. End the chat")
    print("---------------------------")
    try:
        return(int(input("Enter the number what you are interested in[1-3]: ")))
    except :
        print("Only enter choice from 1, 2and 3")
        return 0

def information():
    print("Select Your choice from 1 to 11")
    def upcoming_skills():
        print("1. Artificial Intelligence")
        print("2. Machine Learning and Data Analytics")
        print("3. Cyber Security and Ethical Hacking ")
        print("4. Mobile App Development")
        print("5. Software Development")
        print("6. Cloud Computing and SaaS")
        print("7. BlockChain Development")
        print("8. IT Education")
        print("9. Robotics and Automation")
        print("10.Biotechnology")
        print("11. End chat")
        print("---------------------------")
        try:
            return(int(input("Select Your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def ArtificialIntelligence():
        print("Artificial Intelligence ==> Voice assistants such as Google assistant, Alexa, or Cortana are just the beginning. The future is going to see even more more innovations. We’ve seen AI increasingly enter all fields of life. You can order a pizza or book a cab with just a voice command nowadays AI has certainly been making lives convenient for people over the last couple of years, so it’s no surprise staffs would need to be competent in the field of artificial intelligence in subsequent years. The study of AI should help employees find excellent jobs in IT industries. Even though some people are skeptical about the use of AI as they think the use of robots may put employment at risk, it’s not entirely true. In fact, by 2020, AI is expected to create 2.3 million jobs in the U.S..")
        print("--------------------------------------")


    def MachineLearningandDataAnalytics():
        print("Establishing a brilliant customer and client relationship is going to be a lot easier as machine learning constantly helps us predict many aspects of a customer accurately. In fact, it will help us predict many important things in advance and with such an accuracy that we don’t have to think twice about it. With Big Data and the Internet of Things (IoT) increasingly being used together these days, the future is bright and a lot of stunning advancement is expected to come our way. However, this will only be possible with exceptionally fast and accurate data analysis. Inaccurate data analysis, on the other hand, can cause severe damage. As such, there is a huge need for brilliant IT workers fluent in machine learning and data analytics who can handle data efficiently and produce any desired results.")
        print("--------------------------------------")


    def CyberSecurityandEthicalHacking():
        print(" The Wanna Cry Ransomware attack shook up the world with 2,00,000 systems affected across 150 countries. It was just an eye opener and brought home the fact that cyber security needs improvement. Thus, there is a constant requirement for competent IT professionals with a deep knowledge of network security and firewalls. Most importantly, there will be a huge need for strategists who are well versed in ethical hacking. The knowledge of ethical hacking eventually will help in predicting and keeping up with advancements in the hacking world. That way, strategists can produce the best and most effective cybersecurity products to prevent every possible attempt of intrusion in the future. ")
        print("--------------------------------------")


    def MobileAppDevelopment():
        print("There has been outstanding growth in the e-commerce industry over the years. With more growth expected in the industry in subsequent years, businesses will need innovative and interactive apps that will require better and more advanced approaches to mobile app development. This will drive demand for competent and creative mobile app developers. Developers with an excellent command of multiple programming languages such as Java, C++, C++, and Python, as well as UI and UX designs, are expected to be in huge demand in the coming years.")
        print("--------------------------------------")

    def SoftwareDevelopment():
        print("It’s almost hard to imagine an organization that doesn’t use IT functions. Software development will continue to evolve with organizations’ constant need for ever more advanced software. This will require competent and proficient developers with an exceptional command over multiple programming languages who can keep up with organizations’ increasing software needs and global trends in software development.")
        print("--------------------------------------")

    def CloudComputingandSaaS():
        print("With the extensive use of cloud hosting and dedicated servers, as well as the growing need for virtualization in Amazon AWS, Microsoft Hyper-V, and VMware for private cloud hosting, there will be a constant need for IT workers competent in cloud computing and software-as-a-service (SaaS). Knowledge of virtualization, DevOps, containers, the entire cloud stack, and IPv6 will be an asset for those entering the IT industry.")
        print("--------------------------------------")

    def BlockChainDevelopment():
        print("The blockchain and cryptocurrency sector is new, but a lot of advancement is anticipated in this area in subsequent years. With the growing popularity of cryptocurrency over the last year, companies will be looking for competent developers with knowledge of BlockChain and smart contracts who can build decentralized applications. So improving comprehension about BlockChain and knowledge of multiple programming languages such as DAPP, Peer to Peer Networking, Node.js basics, Public Key Cryptography, and Solidity should prove to be lucrative in the near and long term.") 
        print("--------------------------------------")

    def ITEducation():
        print("With technology making huge leaps, there’s an increasing need for more competent IT educators who can explain complex technologies in simple ways. In fact, tremendous growth in the IT education sector is anticipated in subsequent years.")
        print("--------------------------------------")

    def RoboticsandAutomation(): 
        print("With constant advancement in robotics and automation, many industries will get advanced machines that can bring about a signficant savings in time, effort, and cost. Although there has been fear around the idea of mechanization since the Industrial Revolution, machines can bring about a massive elevation in productivity by eliminating manual repetitive tasks and replacing them with automation. This leads to the necessity for workers with a command over robotics and automation skills in coming years.")
        print("--------------------------------------")


    def Biotechnology():
        print("Biotechnology (a blend of biology and technology) is increasingly popular as innovations such as advanced vaccine production and genetic modification have proven to be massively effective in making lives healthier over the years. As such, the future of biotechnology is bright with many brilliant career options for promising biotechnology students.")
        print("--------------------------------------")





    def print_list():
        option=upcoming_skills()
        while option!= 11:
            if option == 1:
                ArtificialIntelligence()
            elif option == 2:
                MachineLearningandDataAnalytics()
            elif option == 3:
                CyberSecurityandEthicalHacking()
            elif option == 4:
                MobileAppDevelopment() 
            elif option == 5:
                SoftwareDevelopment()
            elif option == 6:
                CloudComputingandSaaS()
            elif option == 7:
                BlockChainDevelopment()
            elif option == 8:
                ITEducation()
            elif option == 9:
                RoboticsandAutomation()
            elif option == 10:
                Biotechnology()    

            else:
                return "Invalid Input"
            option=upcoming_skills()
    print_list()

def lat_tre():
    print("Select Your choice from 1 to 11")
    def tre_lat():
        print("1.Complex problem-solving. ")
        print("2.Critical thinking ")
        print("3.Creativity.")
        print("4.People management.")
        print("5.Coordinating with others.")
        print("6.Emotional intelligence")
        print("7.Judgement and decision-making")
        print("8.Service orientation.")
        print("9.Negotiation.")
        print("10.Cognitive flexibility.")
        print("11. End chat")
        print("------------------------")
        try:
            return(int(input("Select Your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def Complexproblemsolving():
        print("Topping the list as the most desired skill to have by 2020 is complex problem-solving ability — defined by the report as the capacity ‘to solve novel, ill-defined problems in complex, real-world settings.’")
        print("What does that even mean?")
        print("In a nutshell, it’s about having the mental elasticity to solve problems we’ve never seen before, and being able to solve them in a landscape that’s changing at breakneck speed and getting more complex by the minute!")
        
        print("In a world filled with what economists describe as ‘wicked’ problems — problems that are not ‘evil’, but considered wicked because they are near-impossible to solve due to incomplete, contradictory or ever-evolving requirements (think climate change, poverty or terrorism) — complex problem-solvers will be in hot demand.")
        print("As the report details, ‘More than one third (36%) of all jobs across all industries are expected by our respondents to require complex problem-solving as one of their core skills.’")
        print("Now, don’t worry! This doesn’t mean that you’ll be expected to solve the world’s problems. Having strong complex problem-solving skills is about being able to see the big picture, zero in on minute details, and move things around to make a difference.")
        print("Thankfully this is not a skill that anyone is born with. It’s something that gets honed over time, and is built on a strong foundation of critical and lateral thinking. ")
        print("So how do you acquire this holy grail of all skills? According to some studies, problem-solving skills can be improved by playing a lot of video games!")
        print("As our world and the workforce continue to rapidly evolve, it’s clear that we all need to develop alongside it if we’re going to keep apace with the changes. As Doc Emmett Brown put it in Back to the Future, ‘Where we’re going, we don’t need roads!’")
        print("--------------------------------------")


    def Criticalthinking():
        print("Being a critical thinker will still be a valued skillset in the next four years, according to the survey. But what does critical thinking actually involve?")
        print("The answer is: logic and reasoning. Critical thinking involves being able to use logic and reasoning to interrogate an issue or problem, consider various solutions to the problem, and weigh up the pros and cons of each approach.")
        print("While IBM’s supercomputer Watson and its legal-savvy companion ROSS are giving humans a run for their money in the critical thinking department, organisations in 2020 will see critical thinkers as highly employable, and a welcome addition to any team.")
        print("--------------------------------------")


    def Creativity():
        print("As the World Economic Forum senior writer, Alex Gray explains, ‘With the avalanche of new products, new technologies and new ways of working, employees are going to have to become more creative in order to benefit from these changes.’")
        print("Robots may help us get to where we want to be faster, but they can’t be as creative as humans (yet).’")
        print("Creativity is predicted to become a key skill in the future, so before you dismiss yourself as a ‘non-creative’ person, remember that creativity is not the exclusive domain of artsy types like musicians and writers.")
        print("If you’re able to connect the dots with seemingly disparate information, and throw all the ideas together to present something ‘new’, then you are a creative person.")
        print("The problem with the creative process is its inherent ‘non-process’ nature. There is simply no one way to creatively problem-solve something. In saying that, there are ways to unleash the creative within you by exercising curiosity and self-expression on a regular basis.")
        print("Some other things you can do include giving yourself time to let your thoughts wander (this is why some of our best ideas come to us in the shower!), making it a habit to sit down and create a body of work when you’re sleepy (because when your brain’s unfocused, it’s less inhibited), and using limitations as a starting point for creativity!")
        print("--------------------------------------")


    def Peoplemanagement():
        print("Irrespective of how many jobs get automated and how advanced artificial intelligence becomes, employees will always be a company’s most prized resource.")
        print("Human beings are more creative, better at reading each other, and able to piggyback off each other’s ideas and energy. But being human also means that we get sick, we get demotivated, and we get distracted.")
        print("So it’s vital that in the future, managers and team leaders know how to motivate their teams, maximise their productivity and respond to their needs.")
        print("Being a great manager has a lot to do with emotional intelligence, knowing how to delegate, and developing your own management style.")
        print("--------------------------------------")

    def Coordinatingwithothers():
        print("Social skills dominate the list again at number 5, and point to the emerging trend of companies putting more emphasis on strong interpersonal skills, and employees who play well with others.")
        print("Collaboration is crucial in any work environment and this is something that thankfully humans are still better at than robots!")
        print("‘Human interaction in the workplace involves team production, with workers playing off of each other’s strengths and adapting flexibly to changing circumstances,’ the WEF report explains. ‘Such non-routine interaction is at the heart of the human advantage over machines.’")
        print("Coordinating with others involves strong communication skills, an awareness of other people’s strengths and weaknesses, and being able to work with a range of different personalities.")
        print("--------------------------------------")


    def  Emotionalintelligence():
        print("The overwhelming response from HR officers and company strategists was that when it comes to desirable skillsets, ‘overall, social skills—such as persuasion, emotional intelligence and teaching others — will be in higher demand across industries’ of the future.")
        print("Co-author of Emotional Intelligence 2.0, Travis Bradberry explains that emotional intelligence ‘is the other kind of smart.’ It’s that intangible ‘something’ that helps us tune into the kaleidoscope of human emotions, and measures how adept we are at adjusting our behaviour depending on the mood of a colleague, partner, family member, or even our own internal feelings")
        print("Emotional intelligence literally informs every interaction we have. As Bradberry explains in an article for Forbes, ‘It affects how we manage behaviour, navigate social complexities, and make personal decisions that achieve positive results.’")
        print("It’s a social skill that’s particularly important to managers and leaders, and you’ll be glad to hear that you can give your EQ (emotional quotient) a boost!")
        print("-----------------------------------------")
    def Judgementanddecisionmaking():
        print("The ability to make sound judgement calls and the knack for strong decision-making skills is forecast to move up the list to nab the seventh spot by 2020")
        print("This isn’t surprising considering the sheer volume of data that organisations can now amass, and the growing need for employees who can sift through the numbers, find actionable insights, and use big data to inform business strategy and decisions.")
        print("How can you improve your decision-making skills immediately? Start getting a whole lot more comfortable with data. First, figure out what questions or problems you want to answer, then set aside time to explore new data tools and technologies that can help you collect this information. Once you have these two things, you’ll want to make Excel your best friend, learn how to manipulate the data and mine it for all it’s worth!")
        print("-----------------------------------------")


    def Serviceorientation():
        print("Defined as the ability to ‘actively loo[k] for ways to help people,’ having strong service orientation skills is all about shining a spotlight on consumers, and anticipating what their needs will be in the future.")
        print("As the WEF report points out, businesses in the energy, financial services and IT industries are ‘increasingly finding themselves confronted with new consumer concerns about issues such as carbon footprints, food safety, labour standards and privacy.’")
        print("From a skills perspective this means that businesses ‘will need to learn to more quickly anticipate these new consumer values, to translate them into product offerings and to become ever more knowledgeable about the processes involved in meeting these demands.’")
        print("Getting a grip on service orientation involves stepping into the minds of users and thinking about what they value, fear, and dislike; and developing new products or adapting services to future proof your company or brand.")
        print("-----------------------------------------")


    def Negotiation():
        print("With robots infiltrating the workforce and job automation flagged to become increasingly commonplace, social skills will be more important than ever in the future")
        print("Why? Because we’re far better at social interaction and negotiations than robots are (for the time being, anyway).")
        print("Why? Because we’re far better at social interaction and negotiations than robots are (for the time being, anyway). Even people in purely technical occupations will soon be expected to show greater interpersonal skills, and being able to negotiate with your colleagues, managers, clients and teams will be high up on the list of desirable skills.")
        print("To find out how to become a better negotiator, here are five things great negotiators always do.")
        print("1.Sit on the same side of the table.")
        print("2.Depersonalize positions into problems.")
        print("3. Address the why behind the what.")
        print("4. Introduce objective standards.")
        print("5. Have an alternative plan.")
        print("-----------------------------------------")


    def Cognitiveflexibility():
        print("Cognitive flexibility is all about being a mental gymnast. If you think of your brain as a gymnast’s floor, and imagine all the different apparatuses (e.g. the rings, parallel bars, and balance beam) as the different ways of thinking (e.g. the creative brain, mathematical brain, critical thinking brain etc.) — cognitive flexibility is how quickly (and easily) you can swing, leap and twirl back and forth between different systems of thought.")
        print("The more limber you are, the easier it becomes to see new patterns, and to make unique associations between ideas. It sheds new light on the concept of having a ‘nimble’ mind!")
        print("So how do we flex our cognitive muscles? By learning new things and in particular, learning new ways of thinking. If you’re ‘not a creative type’, make it a point to learn an instrument, take up hip-hop dancing or try your hand at an art class. If you’ve got the soul of a creative, but your eyes glaze over when you hear words like ‘financial markets’ or ‘the economy’, make it your mission to read The Economist or The American Economic Review.")
        print("Expand your interests, read outside your comfort zone, and embrace people who challenge your worldviews. Your career (and your brain) will thank you for it.")
        print("--------------------------------------------")
        








    def skill_2020():
        option=tre_lat()
        while option!= 11:
            if option == 1:
                Complexproblemsolving()
            elif option == 2:
                Criticalthinking()
            elif option == 3:
                Creativity()
            elif option == 4:
                Peoplemanagement()
            elif option == 5:
                Coordinatingwithothers()
            elif option ==6:
                Emotionalintelligence()
            elif option ==7:
                Judgementanddecisionmaking()
            elif option == 8:
                Serviceorientation()
            elif option ==9:
                Negotiation()
            elif option == 10:
                Cognitiveflexibility()    

            else:
                return "Invalid Input"
            option=tre_lat()
    skill_2020()
    
def chatbot():
    print("This bot helps you to know the Top 10 Upcoming IT Skills")
    name = input("Enter your name : ") 
    welcome(name)
    print("select your choice")
    choice = show_opt()
    while choice != 3:
        if choice == 1:
            information()
        elif choice == 2:
            lat_tre()
        else:
            print("Please enter the number between 1 to 3")
        choice = show_opt()
        
chatbot()
