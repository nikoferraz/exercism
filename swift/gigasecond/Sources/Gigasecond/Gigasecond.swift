// Import NSDate 

import Foundation
//Solution goes in Sources
// Return the data after a gigasecond has passed
class Gigasecond{

    let gigasecond = 1_000_000_000
    let gsDate: Date
    
    init?(from: String) {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"
        guard let gsDate = formatter.date(from: from) else {
            return nil
        }
        self.gsDate = gsDate
    }
    
    var description: String {
        let gsDate = self.gsDate.addingTimeInterval(TimeInterval(gigasecond))
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"
        return formatter.string(from: gsDate)
    }
}