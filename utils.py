def get_vocab(vocab_path,tags_path):
    
    vocab = {}
    
    with open(vocab_path) as f:
        for i,l in enumerate(f.read().splitlines()):
            vocab[l] = i
    vocab["<PAD>"] = len(vocab)
    
    tag_map = {}
    
    with open(tags_path) as f:
        for i,t in enumerate(f.read().splitlines()):
            tag_map[t]=i
            
    return vocab,tag_map

def get_params(vocab,tag_map,sentences_file,labels_file):
    
    sentences = []
    labels = []
    
    with open(sentences_file) as fp:
        for sentence in fp.read().splitlines():
            s = [vocab[token] if token in vocab else vocab["UNK"] for token in                          sentence.split(' ')]
            sentences.append(s)
        
    with open(labels_file) as fp:
        for sentence in fp.read().splitlines():
            l = [tag_map[label] for label in sentence.split(' ')]
            labels.append(l)
            
    return sentences,labels,len(sentences)
            
