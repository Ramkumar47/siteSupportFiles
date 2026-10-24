#!/bin/julia
#==============================================================================
SLFN with single input and output training

Ramkumar
Sat Oct 24 03:42:31 PM IST 2026
==============================================================================#

using Random
using Plots
using DataFrames
using CSV

#=============================================================================#

# generating training data function
y(x) = 1.5 + 0.6*sin(2*pi*x) + 0.4*sin(2*pi*2.3*x + 0.5) + 0.3*sin(2*pi*4.7*x + 1.2) + 0.2*sin(2*pi*7*x)

# generating x array in linspace
x = LinRange(-2,3,1001)

# number of neurons
N = 20

# number of epochs
epochs = 20000

# learning rate
lr = 0.01

# randomnly initializing weights
Random.seed!(1)
w2 = rand(N) # weights from hidden to output layer
w1 = rand(N) # weights from input to hidden layer
b1 = rand(N) # bias for hidden layer

# reading weights and bias from file if exists
if isfile("weights.csv")
    println("reading weights and bias from file...")
    df = CSV.read("weights.csv",DataFrame)
    w1 = df.w1
    b1 = df.b1
    w2 = df.w2
end

# defining activation function
sigmoid(x) = 1/(1 + exp(-x))

# defining network function
Net(x) = sum(w2 .* sigmoid.(w1 .* x .+ b1))

# begining batch training
xTrain = shuffle(x)
for epoch in 1:epochs
    global w2,w1,b1
    # initalizing cost function
    cost = 0.0
    # looping through data
    for i in 1:length(xTrain)
        xi = xTrain[i]
        # forward pass
        yHat = Net(xi)

        # computing loss
        L = 1/2*(y(xi) - yHat)^2
        cost += L/length(xTrain)

        # computing loss gradients
        dLdW2 = -(y(xi) - yHat).*sigmoid.(w1.*xi .+ b1)
        dLdW1 = -(y(xi) - yHat).*w2.*sigmoid.(w1.*xi .+ b1).*(1 .- sigmoid.(w1.*xi .+ b1)).*xi
        dLdB1 = -(y(xi) - yHat).*w2.*sigmoid.(w1.*xi .+ b1).*(1 .- sigmoid.(w1.*xi .+ b1))

        # updating weights and bias
        w2 -= lr*dLdW2
        w1 -= lr*dLdW1
        b1 -= lr*dLdB1

    end

    print("Epoch: $epoch, Cost: $cost\n")
end

# performing inference for plotting
yHat = [Net(xi) for xi in x]

println("saving estimated data...")
# saving estimated data to csv
fid = DataFrame(
    x = x,
    y = y.(x),
    yHat = yHat
)
CSV.write("estimation.csv",fid)
println("saving weights...")
df = DataFrame(
    w1 = w1,
    b1 = b1,
    w2 = w2
)
CSV.write("weights.csv",df)

# plotting graphs
println("plotting graphs...")
p = plot(size=(800,600),dpi=150)
plot!(p,x,y.(x),label="Target",color=:blue)
plot!(p,x,yHat,label="Predicted",color=:red)

savefig(p,"estimation.png")

print("End")


#=============================================================================#
