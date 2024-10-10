import util
import hashlib

if __name__=="__main__":
    string, hf = util.get_args().input, util.get_args().function
    print("Hash value for `" + string + "` using `" + hf + "` is: " + util.generate_hash(hf, string))
    
