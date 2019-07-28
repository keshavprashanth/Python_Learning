"""Write a function that counts the number of alphabetic characters (a through z, or A through Z)
in your text and then keeps track of how many are the letter ‘e’.
Your function should print an analysis of the text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'

"""

var = """Warren Edward Buffett (/ˈbʌfɪt/; born August 30, 1930)[2] is an American business magnate, investor, speaker and philanthropist who serves as the chairman and CEO of Berkshire Hathaway. He is considered one of the most successful investors in the world[3][4] and has a net worth of US$84.4 billion as of November 1, 2018, making him the third-wealthiest person in the world.[5]

Buffett was born in Omaha, Nebraska. He developed an interest in business and investing in his youth, eventually entering the Wharton School of the University of Pennsylvania in 1947 before transferring and graduating from University of Nebraska at the age of 19. He went on to graduate from Columbia Business School, where he molded his investment philosophy around the concept of value investing that was pioneered by Benjamin Graham. He attended New York Institute of Finance to focus his economics background and soon after began various business partnerships, including one with Graham. He created the Buffett Partnership after meeting Charlie Munger, and his firm eventually acquired a textile manufacturing firm called Berkshire Hathaway and assumed its name to create a diversified holding company.

Buffett has been the chairman and largest shareholder of Berkshire Hathaway since 1970,[6] and he has been referred to as the "Wizard", "Oracle", or "Sage" of Omaha by global media outlets.[7][8] He is noted for his adherence to value investing and for his personal frugality despite his immense wealth.[9] Research published at the University of Oxford characterizes Buffett's investment methodology as falling within "founder centrism" – defined by a deference to managers with a founder's mindset, an ethical disposition towards the shareholder collective, and an intense focus on exponential value creation. Essentially, Buffett's concentrated investments shelter managers from the short-term pressures of the market.[10]

Buffett is a notable philanthropist, having pledged to give away 99 percent[11] of his fortune to philanthropic causes, primarily via the Bill & Melinda Gates Foundation. He founded The Giving Pledge in 2009 with Bill Gates, whereby billionaires pledge to give away at least half of their fortunes.[12] He is also actively contributing to political causes, having endorsed Democratic candidate Hillary Clinton in the 2016 U.S. presidential election;[13] he has publicly opposed the policies, actions, and statements of the current U.S. president, Donald Trump."""


def alphabet_e_counter(var):
    total_alphabet = 0
    total_e = 0
    for char in var:
        if char.isalpha():
            total_alphabet = total_alphabet + 1
            if char == 'e':
                total_e = total_e + 1

    percentage_e = (total_e / total_alphabet) * 100

    print("Your text contains", total_alphabet, "alphabetic characters, of which", total_e, "(", percentage_e, "%) are 'e'")

alphabet_e_counter(var)

