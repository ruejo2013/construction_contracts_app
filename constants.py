import os

class Constants:
    
    DETA_KEY = "<input deta key>"
    LOTTIE_CONSTRUCTION = "https://assets8.lottiefiles.com/packages/lf20_1lvsledo.json"
    LOTTIE_FILE = "lottie_contruction.json"
    IMG_CONSTRUCTION = "images/contruction.png"
    IMG_COMPLEX = "images/shopping_complex.png"

    CONTRACT_DETAILS =['Contract_id', "Invoice_number", "Amount"]
    CURRENCY_ = "USD"
    PAGE_TITLE = "Construction Expense and Payment tracker"
    PAGE_ICON = ":money_with_wings:"
    LAYOUT = "centered"
    INVOICE_FORM = """
        <form action="https://formsubmit.co/<add email address here>" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Contract ID" required>
            <input type="text" name="name" placeholder="Type Your Name Here" required>
            <input type="email" name="email"  placeholder="Your Email" required>
            <textarea name="message"  placeholder="Message should include your Invoice number" required></textarea>
            <button type="submit">Send</button>
        </form>
            """
    MILESTONES = [
        'First Milestone', 'Second Milestone', 'Third Milestone',
        'Forth Milestone', 'Fifth MileStone'
        ]
    WHO_WE_ARE =  """
            # Who We Are
            - We make construction contract ***payment easy***.
            - We guarantee that your payments will be issued on time.
            - A burden free way of doing business.
            """
    CONTRACTORS_ID = [
        'Contract ID', 'AB276NYC', 'TX674HU', 'BU456MUS', 
        'NJ465AV', 'NJ456NW', 'CO5278PS', 'ML7465NU'
        ]
    ACCOUNT_NUMBER = ['Select Account',
        '0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db',
        '0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB']