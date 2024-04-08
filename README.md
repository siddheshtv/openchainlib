# openchainlib

`openchainlib` aims to reduce machine learning training time by introducing decentralized worker nodes that get rewarded for the computational power they provide. While keeping training costs low, the aim of this library is to contribute towards faster model training and machine learning development.

## Why?

- Training an ML model is extremely time consuming
- Using cloud services might get too costly over time

## Definitions

`openchainlib` works on a client-worker architecture.

Client node - The client would want to train a machine learning model but does not have ample amount of resources to either get the training done faster, or cheaper.

Worker node - A worker is someone who is willingly participating to give away computational power in return for a reward.

Job - A job is something that requires compute power. In our case, this is the machine learning pipeline.

Block - A block consists of `n` number of jobs. Each block has it's own unique reward amount which is dependant on the various factors that include: amount of jobs, expected compute power required, time consumed to solve the block, and more.

OhChain! coin - It is the fundamental currency of the `openchainlib` ecosystem. Client nodes that want to get a job done, need to pay the amount in OhChain! coins.

Gas - Gas is a fee structure introduced in order to maintain validity, governance, and security in the `openchainlib` network. Gas is a reward that is paid to Validator nodes in return for verifying the authenticity of each block.

Proof-of-History - `openchainlib` works on a Proof-of-History mechanism.

Validator node - A validator node is responsible for verifying the hash values of each block. One cannot directly become a validator node until and unless they hold a stake of more than 39900 in the network. There can only be 239 validator nodes in the entirety of the `openchainlib` ecosystem.
