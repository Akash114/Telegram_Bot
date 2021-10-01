import os

import telebot
import json
from web3 import Web3
from telebot.types import InputMediaPhoto, InputMediaVideo

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')


bot = telebot.TeleBot(TOKEN,
                      parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


#Contract of Grice Stake Details
def get_contract():
    f = open('StakingToken.json', "r")

    w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org:443'))

    currentAbis = json.loads(f.read())

    address = w3.toChecksumAddress(os.getenv('ADDRESS'))

    contract = w3.eth.contract(address=address, abi=currentAbis['abi'])
    return contract


@bot.message_handler(commands=['community_rules'])
def send_welcome(message):
    msg = """   📜📜 GRISE COMMUNITY RULES📜📜 
    -  Is the comment about GRISE FINANCE? No? Consider posting it elsewhere. 
    
    -  We look for individuals who are NET POSITIVE contributors to the group. If a person is only negative we reserve the right to ban or block that individual. Banning should not be done on the basis of a single comment or post unless it is egregious. 
   
    -  Hate speech, is not permitted, and can result in an instant ban. Please keep discourse civil. 
    
    -  No bad mouthing, no name calling, no disparaging others. 
    
    -  We reserve the right to moderate,block or remove posts that contain factual inaccuracies or unsubstantiated claims. 
    
    -  Spamming, especially off topic, will result in an instant ban.
    
    -  Instant BAN: impersonation, discrimination, explicit content, promotional links, spam, bots, or outright scams 
    
    -Please take any price discussion or promotion offers to this channel. We will have a person of our team monitor this. https://t.me/unofficialgrise """
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['introduction'])
def send_intro(message, content_types=['video']):
    msg = """
        Welcome to Grise finance platform. Our platform is established on the intersection of ai and Blockchain. 
        
        Our first product being AI trading platform to help improve your trading experience and make smarter investment decisions.
        
        Our software analyzes different data points and sentiment of different media channels to predict different analytics on crypto currencies.
        
        At the core of our platform economy is grise token and GRISE N F T.Which forms the basis of grise platforms economic system.
    """
    video = open('Grise introduction.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['tokenomics'])
def send_intro(message, content_types=['video']):
    msg = """
    Grise token is both inflationary and deflationary in nature At the time of this video there are a total of 265,207 circulating and total supply.
    
    The inflation of 6 percent of the total supply per year is distributed between medium term and long term stakers.
    
    The deflation comes from slight burn incorporated on the transaction fees and stake cancellation penalty
    """
    video = open('Tokenomics.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['transaction_fees'])
def send_intro(message, content_types=['video']):
    msg = """
        Grise token has a transaction fees of point 3 percent on the buy side and 3.47 percent on the sell side.
        
        The distribution of 3.47 percent fees is as follows.
        
        point nine one percent goes to all token holders and stakers
        
        point five seven percent goes to any medium term and long term stakers
        
        1.06 percent goes to a reservoir
        
        point five zero percent goes for operations
        
        point 43 percent goes to a burn address.
        
        on the buy side point one percent goes to burn address point 2 percent goes to operations.
    """
    video = open('Transaction Fees.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['short_term_staking'])
def send_short_term_staking_updated(message, content_types=['video']):
    msg = """
        Short term staking allows participant to stake their Grise tokens for 1 week or an increment of 1 week up to 12 weeks. 
        
        Short term staking has the following advantages. 
        
        At the end of the contract, stakers will be compensated with an extra 2% of their tokens to reduce their sell side transaction fee
        
        Short-term stakers will also be eligible for a small portion of the transaction fees,and penalties from contract breaks.
        
        Lastly, as a short-term staker, you will get full access to Grise’s AI price prediction platform.
        """
    video = open('Short Term Staking Updated.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['staking_structure'])
def send_staking_structure_update(message, content_types=['video']):
    msg = """
        Grise has 3 kinds of staking available,
        short term, medium term and long term
        
        Short term staking has a total of 1250 spots
        
        Medium term staking has a total of 1041 spots
        
        And long term staking has a total of 300 spots
        
        Note:- Once the slots are filled someone will have to cancel their stake or finish it for the next person to enter. 
        """
    video = open('Staking Structure Update.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['medium_term_staking'])
def send_medium_term_staking_updated(message, content_types=['video']):
    msg = """
        Medium-term staking allows participants to stake their Grise tokens for 3 months or an increment of 3 months, up to 9 months. Staking on a medium-term period offers users the following advantages:
        
        At the end of the staking period, stakers are free to sell their tokens at any time without incurring any transaction fees. This is achieved by issuing stakers an extra 3.47% of their tokens at the end of the staking contract.
        
        Medium term stakers will be eligible for a greater portion of transaction fees and also a portion of stake cancellation penalty rewards.
        
        Medium term stakers will also receive a 30 percent of the total yearly supply inflation rewards as well as 30 percent of the reservoir rewards.
        
        Finally, medium-term stakers will have full access to Grise’s AI price prediction platform.
        """
    video = open('Medium Term Staking Updated.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['long_term_staking'])
def send_long_term_staking_updated(message, content_types=['video']):
    msg = """
        Long-term staking allows participants to stake their Grise tokens for 1 year or an increment of 1 year up to 10 years. Staking on a long-term period offers users the following advantages:
        
        At the end of the staking period, stakers are free to sell their tokens at any time without incurring any transaction fees. This is achieved by issuing stakers an extra 3.47% of their tokens at the end of the staking contract.
        
        Long term stakers will be eligible for a greater portion of transaction fees and also a portion of stake cancellation penalty rewards.
        
        Long term stakers will also receive 70% of the total yearly supply inflation rewards as well as 70 percent of the reservoir rewards
        
        Lastly, long-term stakers will have full access to Grise’s AI price prediction platform
        """
    video = open('Long Term Staking Updated.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)



@bot.message_handler(commands=['stake_info'])
def stake_info(message):
    contract = get_contract()
    stake_left = contract.functions.getSlotLeft().call()
    msg = "Short-term staking Slots available : " + str(stake_left[0]) + "\nMedium-term staking Slots available : " + str(
        stake_left[1] + stake_left[2] + stake_left[3]) + "\n\t- 3-Month : " + str(stake_left[1]) + "\n\t- 6-Month : " + str(
        stake_left[2]) + "\n\t- 9-Month : " + str(stake_left[3]) + "\nLong-term staking Slots available : " + str(stake_left[4])
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['stake_cancellation_penalty'])
def send_intro(message, content_types=['video']):
    msg = """
        The Grise contract allows a participant to close a stake at any time. However, if the participant closes the stake within the staking period, he/she will incur a 17% penalty. The penalty will work on a sliding scale. 
        
        For instance, if a staker closes a stake on the first day of it being Active, he/she will receive a 17% penalty applied to their principal. 
        
        If the same stake is closed on the day before the contract ends, the staker will receive a 1.7% penalty applied to their principal. 
        
        The penalty fee will be distributed as follows: 34.27% of cancellation penalty will go to a reservoir, 25.62% will be distributed in the form of grise token to all mid-term and long term stakers, 15.00% will go to operational expenses, 13.00% will be distributed to all the weekly stakers in the form of grise token and the remaining 12% will go to a burn address.
    """
    video = open('Stake Cancellation Penalty.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['token_holders_reward'])
def send_intro(message, content_types=['video']):
    msg = """
    Grise token holder are eligible for a portion of transaction fees.
    
    Token holders  can claim their transaction fee rewards every 7th day for 24 hours on the dashboard, if a token holder doesn’t claim their reward within 24 hours their tokens will be burned.
    
    Please display the window we talked about demonstrating the count down for token holders. Ping me if you have any questions on this. I have attached a screen shot below. 
    """
    video = InputMediaVideo(open('Token Holders Rewards.compressed.mp4', 'rb'),caption=msg,supports_streaming=True)
    img = InputMediaPhoto(open('token_holders.png','rb'))

    bot.send_media_group(message.chat.id,[video,img],timeout=10000)


@bot.message_handler(commands=['stakers_rewards_distribution'])
def send_intro(message, content_types=['video']):
    msg = """Grise’s transaction fee and contract break fee rewards are distributed weekly while reservoir rewards are distributed on a monthly basis.  
    
    These rewards can be scraped on your dashboard. Medium term stakers receive 30 percent of the reservoir rewards while long term stakers receive 70 percent of the reservoir rewards. 
   
    Users can stake a day before reward distribution to be eligible for the rewards.
     
     -Note in the video circle scrape rewards from the below picture. """
    video = InputMediaVideo(open('Grise Reward Distribution.compressed.mp4', 'rb'),caption=msg,supports_streaming=True)
    img = InputMediaPhoto(open('stackers rewards.png','rb'))

    bot.send_media_group(message.chat.id,[video,img],timeout=10000)


@bot.message_handler(commands=['grise_nfts'])
def send_intro(message, content_types=['video']):
    msg = """GRISE NFTs give you access to our services. 
    
    Our NFTs are gamified please read through the NFT section on our website for full details. """
    video = open('GRISe NFTs.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['ai_platform'])
def send_intro(message, content_types=['video']):
    msg = """Grise platform’s goal is to utilize and harness the power of AI and integrate it with different products. 
   
    Our first product to be released is Crypto AI Index. Our AI products will be available to stakers and our NFT holders. """
    video = open('AI platform.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)


@bot.message_handler(commands=['team'])
def send_intro(message, content_types=['video']):
    msg = """Grise Team constitutes of a group of blockchain developers, Ai Scientists, many other members working as a team to make GRISE possible. 
    
    We work diligently with goal of innovating new techs that merges between AI and block chain. We welcome you aboard on this Journey with us. """
    video = open('Team.compressed.mp4', 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True, timeout=10000,caption=msg)



try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except:
    exec(open("main.py").read())
