import yt_dlp, requests as web, ast, os, datetime

author = """
--------------------------------------------------

# App Name   :: YouTube Downloader
# Created By :: Thamizhan PS
# Version    :: 1.0
# Contact    :: psthamizhan02@gmail.com
# Github ID  :: https://github.com/psvel6672

--------------------------------------------------
"""

print(author)

YTUrl = input('# Enter YouTube URL :: ')

Dir = 'YTDownloads'

getFormatJSON = ""
fileTitle = ""
fileExt = ""
fileSrc = ""

chkId = False
getId = ""

sId = 1
URLData = []

chkDir = os.path.exists(Dir)

if chkDir == False:
    os.mkdir(Dir)

try:
    loadYTUrl = yt_dlp.YoutubeDL().extract_info(url = str(YTUrl), download=False)
    fileTitle = loadYTUrl['title']
    getFormatJSON = loadYTUrl['formats']

except:
    print('# Not a Valid URL...')

for cons in getFormatJSON:

    ext = ''
    acodec = ''
    abr = ''
    format_id = ''
    format_note = ''
    src = ''

    try:
        ext = cons['ext']
        abr = cons['abr']
        acodec = cons['acodec']
        format_id = cons['format_id']
        format_note = cons['format_note']
        src = cons['url']
    except:
        pass

    if acodec != '' and acodec != 'none' and ext != 'webm' and str(src) != '':
        tmpData = ""
        tmpData = {'id':str(sId), 'ext':str(ext), 'format_id':str(format_id), 'format_note':str(format_note), 'src':str(src)}
        URLData.append(tmpData)
        sId += 1

chkLen = len(URLData)

if int(chkLen) != 0:

    print("\n# Find avilable files list \n--------------------------------------------------")
    
    for slctSRC in URLData:
        tmpSrc = ast.literal_eval(str(slctSRC))
        print("# "+str(tmpSrc['id']) +" :: "+ str(tmpSrc['ext'])+" :: "+str(tmpSrc['format_note']))

    print("--------------------------------------------------")
else:
    print('# No Data Found...')
    chkId = True

while chkId == False:
    getId = input('# Please Select Your ID :: ')

    if float(chkLen) < float(getId):
        print('# Please Enter Valid Id')
    else:
        if int(getId) == 0:
            getId = 1
        chkId = True

for slctSRC in URLData:
    tmpSrc = ast.literal_eval(str(slctSRC))
    if str(tmpSrc['id']) == str(getId):
        fileExt = str(tmpSrc['ext'])
        fileSrc = str(tmpSrc['src'])

if str(fileSrc) != "":
    print("# Please Wait File Downloading...")

    now = datetime.datetime.now().strftime("%b%d%Y_%I_%M_%S_%p")
    audioFileName = str(fileTitle)+'_'+str(now)+'.'+str(fileExt)
    audioFilePath = r'./'+str(Dir)+'/'+str(audioFileName)
    
    getAFContent = web.get(fileSrc)
    with open(audioFilePath, 'wb') as af:
        af.write(getAFContent.content)

    print('# File Download Successfully.')
    print('# File Path :: '+str(audioFilePath))
    
else:
    print('# Error Found')
