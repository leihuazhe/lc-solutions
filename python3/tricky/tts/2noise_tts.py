import ChatTTS
from IPython.display import Audio

content = """
Hi, I'm [Your Name], and I'm a seasoned Backend Engineer with extensive experience in developing and optimizing complex systems. I have a solid background in Java and Scala, which has allowed me to work on enhancing system performance, data security, and scalability throughout my career.
Regarding my skills, I am proficient in Java and Scala. In terms of technologies, I have experience with microservices, distributed systems, JavaAgent, full-link stress testing, RPC frameworks, and real-time data monitoring. My methodological approaches include both functional programming and object-oriented programming.
My professional journey started at Hengxin Automotive E-commerce Co., Ltd, where I worked as a Java Developer from August 2013 to June 2014. Here, I led the development of the company's unified data reporting dashboard, enhancing data analysis by 40%, and optimized various reporting processes, reducing report generation time by 25%.
After that, I joined Today Technology Center as a Senior Java Developer from July 2014 to February 2015. I developed core infrastructure components and an order management platform, which improved operational efficiency by 30%.
I then moved to Xiaomi Technology Co., Ltd, where I served as a Backend Engineer from March 2015 to August 2016. I enhanced their advertising data monitoring system, improving key metric accuracy by 25%, and increased advertising revenue by 20%.
Next, at Yunji Inc., I worked as a Senior Java Developer from September 2016 to November 2018. I boosted microservice gateway performance by 40% and improved service stability by 35% through advanced monitoring systems. Additionally, I increased deployment efficiency by 20% by developing a distributed call chain tracking system.
Currently, I am with Sensors Data Technology Co., Ltd, where I have been working as a Backend Engineer since December 2018. Here, I improved user data privacy protection by 30% through dynamic desensitization, optimized data processing efficiency by 20%, and enhanced system compatibility by 25% through middleware integration.
I am passionate about solving complex technical problems and continuously improving system performance and security. I look forward to contributing my skills to enhance system performance and security in your company, and to work on cutting-edge technologies and challenging projects.
"""

chat = ChatTTS.Chat()
chat.load_models()

texts = [content]

wavs = chat.infer(texts, use_decoder=True)
Audio(wavs[0], rate=24_000, autoplay=True)
