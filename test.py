from openai import OpenAI
client = OpenAI()



# Text and prompt. 
Text="""
海洋可持续发展战略
中国有12亿多人口，陆地自然资源人均占有量低于世界平均水平。根据中国有关方面的统计:中国有960万平方公里的陆地国土，居世界第三位，但人均占有陆地面积仅有0.008平方公里，远低于世界人均0.3平方公里的水平;全国近年来年平均淡水资源总量为28,000亿立方米，居世界第六位，但人均占有量仅为世界平均水平的四分之一;中国陆地矿产资源总量丰富，但人均占有量不到世界人均量的一半。中国作为一个发展中的沿海大国，国民经济要持续发展，必须把海洋的开发和保护作为一项长期的战略任务。
中国拥有太陆岸线18000多公里，以及面积在500平方米以上的海岛5000多个，岛屿岸线14000多公里;按照《联合国海洋法公约》的规定，中国还对广阔的大陆架和专属经济区行使主权权利和管辖权;中国的海域处在中、低纬地带，自然环境和资源条件比较优越。中国海域海洋生物物种繁多，已鉴定的达20278种。中国海域已经开发的渔场面积达81.8万平方海里。中国有浅海、滩涂总面积约1333万公顷，按现在的科学水平，可进行人工养殖的水面有260万公顷，已经开发利用的有93.8万公顷。中国海域有30多个沉积盆地，面积近70万平方公里，石油资源量约250亿吨，天然气资源量约8.4万亿立方米。中国沿海共有160多处海湾和几百公里深水岸线，许多岸段适合建设港口，发展海洋运输业。沿海地区共有1500多处旅游娱乐景观资源，适合发展海洋旅游业。中国海域还有丰富的海水资源和海洋"""
prompt="""
summerise the text in {Text}"""

messages = [
    {"role": "user", "content": Text},
    {"role": "user", "content": prompt}
]



# Processing by openai.
response=client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=messages
)
result = response.choices[0].message.content



# save result and open the txt file automatically.
import os
file_path = r'C:\Users\vhxb\Desktop\output.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(result)
os.startfile(file_path)
