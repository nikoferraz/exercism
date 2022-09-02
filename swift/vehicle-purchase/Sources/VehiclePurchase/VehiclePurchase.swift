func canIBuy(vehicle: String, price: Double, monthlyBudget: Double) -> String {
    let monthlyPayment: Double = price / 60
    let frugalThreshold: Double = monthlyBudget * 1.1
    if monthlyPayment <= monthlyBudget {
        return "Yes! I'm getting a " + vehicle
    } else if monthlyPayment <= frugalThreshold {
        return "I'll have to be frugal if I want a " + vehicle
    }
    return "Darn! No " + vehicle + " for me"
}

func licenseType(numberOfWheels wheels: Int) -> String {
    switch wheels {
    case 2 ... 3:
        return "You will need a motorcycle license for your vehicle"
    case 4 ... 6:
        return "You will need an automobile license for your vehicle"
    case 18:
        return "You will need a commercial trucking license for your vehicle"
    default:
        return "We do not issue licenses for those types of vehicles"
    }
}

func registrationFee(msrp value: Int, yearsOld age: Int) -> Int {
    if age >= 10 {
        return 25
    }
    return Int(max(value, 25_000) - ((value * age) / 10 )) / 100
}
