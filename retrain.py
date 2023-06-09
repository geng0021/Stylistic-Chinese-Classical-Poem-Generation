from dseq_trainer import DSeqTrainer
print('2')
from wm_trainer import WMTrainer
print('2')
from graphs import WorkingMemoryModel
print('2')
from tool import Tool
print('2')
from config import device, hparams
print('2')
import utils
print('2')


def pretrain(wm_model, tool, hps, specified_device):
    dseq_trainer = DSeqTrainer(hps, specified_device)

    print ("dseq pretraining...")
    dseq_trainer.train(wm_model, tool)
    print ("dseq pretraining done!")



def train(wm_model, tool, hps, specified_device):
    last_epoch = utils.restore_checkpoint(
        hps.model_save_to_dir, specified_device, wm_model)

    if last_epoch is not None:
         print ("checkpoint exsits! directly recover!")
    else:
         print ("checkpoint not exsits! train from scratch!")

    wm_trainer = WMTrainer(hps, specified_device)
    wm_trainer.train(wm_model, tool)


def main():
    hps = hparams
    print('1')
    tool = Tool(hps.sens_num, hps.sen_len,
        hps.key_len, hps.topic_slots, hps.corrupt_ratio)
    print('1')
    tool.load_dic(hps.vocab_path, hps.ivocab_path)
    print('1')
    vocab_size = tool.get_vocab_size()
    print('1')
    PAD_ID = tool.get_PAD_ID()
    B_ID = tool.get_B_ID()
    assert vocab_size > 0 and PAD_ID >=0 and B_ID >= 0
    hps = hps._replace(vocab_size=vocab_size, pad_idx=PAD_ID, bos_idx=B_ID)
    print ("hyper-patameters:")
    print (hps)
    input("please check the hyper-parameters, and then press any key to continue >")

    wm_model = WorkingMemoryModel(hps, device)
    utils.restore_checkpoint(hps.model_dir, device,wm_model)
    wm_model = wm_model.to(device)
    wm_model.eval()

    pretrain(wm_model, tool, hps, device)
    train(wm_model, tool, hps, device)


if __name__ == "__main__":
    main()
