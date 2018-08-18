"""
我们可以先遍历一次字符串，这样就可以统计出字符串空格的总数，并可以由此计算出替换之后的字符串的总长度。
每替换一个空格，长度增加2，因此替换以后字符串的长度等于原来的长度加上2乘以空格数目。以"We are happy"为例，
"We are happy"这个字符串的长度为14（包括结尾符号"\n"），里面有两个空格，因此替换之后字符串的长度是18。

我们从字符串的尾部开始复制和替换。首先准备两个指针，P1和P2，P1指向原始字符串的末尾，而P2指向替换之后的
字符串的末尾。接下来我们向前移动指针P1，逐个把它指向的字符复制到P2指向的位置，直到碰到第一个空格为止。
碰到第一个空格之后，把P1向前移动1格，在P2之前插入字符串"%20"。由于"%20"的长度为3，同时也要把P2向前移动3格。
"""


"""class Solution {
public:
	void replaceSpace(char *str,int length) {
		if(str == NULL && length <= 0){
            return;
        }
        /*original_length为字符串str的实际长度*/
        int original_length = 0;			//原始长度
        int number_blank = 0;				//空格数
        int i;
        while(str[i++] != '\0'){				//遍历字符串
            ++original_length;				//长度+1
            if(str[i] == ' '){
                ++number_blank;				//遇到空格+1
            }
        }
        /*new_length为把空格替换成'%20'之后的长度*/
        int new_length = original_length + 2 * number_blank;
        
        int index_original = original_length;	//原始字符串末尾索引值
        int index_new = new_length;				//计算长度后的字符串末尾索引值
        
        /*index_original指针开始向前移动，如果遇到空格，替换成'%20'，否则进行复制操作*/
        while(index_original >= 0 && index_new > index_original){
            if(str[index_original] == ' '){
                str[index_new--] = '0';
                str[index_new--] = '2';
                str[index_new--] = '%';
            }
            else{
                str[index_new--] = str[index_original];
            }
            --index_original;
        }
	}
};"""

# def replaceSpace(s):
#     return s.replace(' ','%20')

def replaceSpace(s):
    length=len(s)
    if length==0:
        return
    original_length=0;
    number_blank=0;
    for i in s:
        original_length+=1
        if i==' ':
            number_blank+=1
    new_length = int(original_length+2*number_blank)
    array=[]
    for i in s:
        array.append(i)
    for i in range(number_blank*2):
        array.append(' ')
    index_original=int(original_length)-1
    index_new=int(new_length)-1
    while(index_original>=0 and index_new>index_original):
        if (array[index_original]==' '):
            array[index_new]='0'
            index_new-=1
            array[index_new]='2'
            index_new-=1
            array[index_new] = '%'
            index_new-=1
        else:
            array[index_new]=array[index_original]
            index_new-=1
        index_original-=1
    s=''.join(str(i) for i in array)
    return s

if __name__=='__main__':
    print(replaceSpace('Hello World'))