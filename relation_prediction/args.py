from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser(description="Relation Prediction")
    parser.add_argument('--relation_prediction_mode', required=True, type=str, help='options are CNN, GRU, LSTM')
    parser.add_argument('--no_cuda', action='store_false', help='do not use cuda', dest='cuda')
    parser.add_argument('--gpu', type=int, default=0) # Use -1 for CPU
    parser.add_argument('--epochs', type=int, default=30)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--dataset', type=str, default="RelationPrediction")
    parser.add_argument('--mode', type=str, default='static')
    parser.add_argument('--lr', type=float, default=1e-4)
    parser.add_argument('--seed', type=int, default=3435)
    parser.add_argument('--dev_every', type=int, default=2000)
    parser.add_argument('--log_every', type=int, default=1000)
    parser.add_argument('--patience', type=int, default=10)
    parser.add_argument('--save_path', type=str, default='saved_checkpoints')
    parser.add_argument('--specify_prefix', type=str, default='id1')
    parser.add_argument('--output_channel', type=int, default=300)
    parser.add_argument('--words_dim', type=int, default=300)
    parser.add_argument('--num_layer', type=int, default=2)
    parser.add_argument('--rnn_dropout', type=float, default=0.3, help='dropout in rnn')
    parser.add_argument('--input_size', type=int, default=300)
    parser.add_argument('--hidden_size', type=int, default=300)
    parser.add_argument('--rnn_fc_dropout', type=float, default=0.3, help='dropout before fully connected layer in RNN')
    parser.add_argument('--clip_gradient', type=float, default=0.6, help='gradient clipping')
    parser.add_argument('--vector_cache', type=str, default="../data/sq_glove300d.pt")
    parser.add_argument('--weight_decay',type=float, default=0)
    parser.add_argument('--cnn_dropout', type=float, default=0.5, help='dropout before fully connected layer in CNN')
    parser.add_argument('--fix_embed', action='store_false', dest='train_embed')
    parser.add_argument('--hits', type=int, default=5)
    # added for testing
    parser.add_argument('--data_dir', type=str, default='../data')
    parser.add_argument('--trained_model', type=str, default='')
    parser.add_argument('--results_path', type=str, default='results')
    args = parser.parse_args()
    return args