import sys
import pytesseract
from difflib import SequenceMatcher as SQ

try:
    from PIL import Image
except ImportError:
    import Image


lang = sys.argv[1]

img_path = '/app/data/ground-truth/3101.tif'
img = Image.open(img_path)
raw_text = pytesseract.image_to_string(img, lang=lang, config='--psm 7')  # make sure to change your `config` if different 
target = """Once apon a time there was a girl named Mary. On a warm 
sunny day Mary was walking through the woods near hear nouse 
to look for some critters to take pictures of. She loved animals 
and nature all her life even though she was only nine years old 
She thinks that she is going to die soon. She does go to school 
but she isn't that smart. For example Mary recycled a pie 
even though the pie was not even bitten. Another thing she did 
was leave her muffin in the woods while she was traveling with  
her family to Andrea's house which is one of Mary's friends at 
school and Mary's muffin was eaten by a bear that sniffed it 
from far away. Yes. Mary could be a little weird but that is 
just how she is. Back to the real story now. Mary found a 
fox, took a picture she also found a rabbit took a picture 
she found a squirrel and took a picture before it ran away. 
But sooner or later she saw two eyes peeking through a bush 
on the side of the path she was walking on. Then the 
creature slowly came out of the bush. It was a bear. The bear 
growled at Mary. Mary was terrifyed. She started running and 
running but she could still see the bear growling behind her. This 
was the end of Mary. Mary was approaching her house she 
could see it now. She was safe in her house. She was now 
really scared. She could possibly be eaten but she made it to 
the door opened it and slammed it shut before the bear could 
get in. She ran or sprinted rather up to her room. "I'm alive!!" 
She cried. I just can't belive it I'm alive!!" Mary was so 
relifed she told her mom and dad and her brother. And that 
night Mary was kissed goodnight and tucked into bed. And that 
is the only brave time of her life."""

print(f"Output: {raw_text}\nPercent coincidence: {round(SQ(None, target, raw_text).ratio()*100,2)}%")
