using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000600: Charles Kim
/// </summary>
public class _11000600 : NpcScript {
    internal _11000600(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 50;60;70;80;90;100;110;120;130
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002402$ 
                // - What can I do for you?
                return true;
            case 50:
                // $script:0831180407002407$ 
                // - You still have your $item:30000145$. Why don't you use it? You won't regret it. 
                return true;
            case 60:
                // $script:0831180407002408$ 
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002409$
                    // - I want another $item:30000145$.
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:0831180407002410$ 
                // - $MyPCName$, you already got a free $item:30000145$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002411$
                    // - Yeah, I want it.
                    case 0:
                        Id = 62;
                        return false;
                    // $script:0831180407002412$
                    // - Never mind, I don't want it.
                    case 1:
                        Id = 63;
                        return false;
                }
                return true;
            case 62:
                // $script:0831180407002413$ 
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002414$
                    // - Yep.
                    case 0:
                        Id = 65;
                        return false;
                    // $script:0831180407002415$
                    // - Nope.
                    case 1:
                        Id = 64;
                        return false;
                }
                return true;
            case 63:
                // $script:0831180407002416$ 
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000145$.
                return true;
            case 64:
                // $script:0831180407002417$ 
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return true;
            case 65:
                // $script:0831180407002418$ 
                // - Good, then it's 10,000 mesos for a $item:30000145$.
                switch (selection) {
                    // $script:0831180407002419$
                    // - Here's the money.
                    case 0:
                        Id = 0; // TODO: 66 | 67
                        return false;
                }
                return true;
            case 66:
                // $script:0831180407002420$ functionID=1 
                // - Here's your $item:30000145$. I hope you enjoy your new home. Bye for now!
                return true;
            case 67:
                // $script:0831180407002421$ 
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return true;
            case 70:
                // $script:0831180407002422$ 
                // - House prices have been dropping lately, attracting many potential buyers. It's kept me quite busy!
                return true;
            case 80:
                // $script:0831180407002423$ 
                // - You still have your $item:30000255$. Why don't you use it? You won't regret it. 
                return true;
            case 90:
                // $script:0831180407002424$ 
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002425$
                    // - I want another $item:30000255$.
                    case 0:
                        Id = 91;
                        return false;
                }
                return true;
            case 91:
                // $script:0831180407002426$ 
                // - $MyPCName$, you already got a free $item:30000255$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002427$
                    // - Yeah, I want it.
                    case 0:
                        Id = 92;
                        return false;
                    // $script:0831180407002428$
                    // - Never mind, I don't want it.
                    case 1:
                        Id = 93;
                        return false;
                }
                return true;
            case 92:
                // $script:0831180407002429$ 
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002430$
                    // - Yep.
                    case 0:
                        Id = 95;
                        return false;
                    // $script:0831180407002431$
                    // - Nope.
                    case 1:
                        Id = 94;
                        return false;
                }
                return true;
            case 93:
                // $script:0831180407002432$ 
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000255$.
                return true;
            case 94:
                // $script:0831180407002433$ 
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return true;
            case 95:
                // $script:0831180407002434$ 
                // - Good, then it's 10,000 mesos for a $item:30000255$.
                switch (selection) {
                    // $script:0831180407002435$
                    // - Here's the money.
                    case 0:
                        Id = 0; // TODO: 96 | 97
                        return false;
                }
                return true;
            case 96:
                // $script:0831180407002436$ functionID=1 
                // - Here's your $item:30000255$. I hope you enjoy your new home. Bye for now!
                return true;
            case 97:
                // $script:0831180407002437$ 
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return true;
            case 100:
                // $script:0831180407002438$ 
                // - You still have your $item:30000254$. Why don't you use it? You won't regret it. 
                return true;
            case 110:
                // $script:0831180407002439$ 
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002440$
                    // - I want another $item:30000254$.
                    case 0:
                        Id = 111;
                        return false;
                }
                return true;
            case 111:
                // $script:0831180407002441$ 
                // - $MyPCName$, you already got a free $item:30000254$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002442$
                    // - Yeah, I want it.
                    case 0:
                        Id = 112;
                        return false;
                    // $script:0831180407002443$
                    // - Never mind, I don't want it.
                    case 1:
                        Id = 113;
                        return false;
                }
                return true;
            case 112:
                // $script:0831180407002444$ 
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002445$
                    // - Yep.
                    case 0:
                        Id = 115;
                        return false;
                    // $script:0831180407002446$
                    // - Nope.
                    case 1:
                        Id = 114;
                        return false;
                }
                return true;
            case 113:
                // $script:0831180407002447$ 
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000254$.
                return true;
            case 114:
                // $script:0831180407002448$ 
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return true;
            case 115:
                // $script:0831180407002449$ 
                // - Good, then it's 10,000 mesos for a $item:30000254$.
                switch (selection) {
                    // $script:0831180407002450$
                    // - Here's the money.
                    case 0:
                        Id = 0; // TODO: 116 | 117
                        return false;
                }
                return true;
            case 116:
                // $script:0831180407002451$ functionID=1 
                // - Here's your $item:30000254$. I hope you enjoy your new home. Bye for now!
                return true;
            case 117:
                // $script:0831180407002452$ 
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return true;
            case 120:
                // $script:0831180407002453$ 
                // - You still have your $item:30000253$. Why don't you use it? You won't regret it. 
                return true;
            case 130:
                // $script:0831180407002454$ 
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002455$
                    // - I want another $item:30000253$.
                    case 0:
                        Id = 131;
                        return false;
                }
                return true;
            case 131:
                // $script:0831180407002456$ 
                // - $MyPCName$, you already got a free $item:30000253$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002457$
                    // - Yeah, I want it.
                    case 0:
                        Id = 132;
                        return false;
                    // $script:0831180407002458$
                    // - Never mind, I don't want it.
                    case 1:
                        Id = 133;
                        return false;
                }
                return true;
            case 132:
                // $script:0831180407002459$ 
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002460$
                    // - Yep.
                    case 0:
                        Id = 135;
                        return false;
                    // $script:0831180407002461$
                    // - Nope.
                    case 1:
                        Id = 134;
                        return false;
                }
                return true;
            case 133:
                // $script:0831180407002462$ 
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000253$.
                return true;
            case 134:
                // $script:0831180407002463$ 
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return true;
            case 135:
                // $script:0831180407002464$ 
                // - Good, then it's 10,000 mesos for a $item:30000253$.
                switch (selection) {
                    // $script:0831180407002465$
                    // - Here's the money.
                    case 0:
                        Id = 0; // TODO: 136 | 137
                        return false;
                }
                return true;
            case 136:
                // $script:0831180407002466$ functionID=1 
                // - Here's your $item:30000253$. I hope you enjoy your new home. Bye for now!
                return true;
            case 137:
                // $script:0831180407002467$ 
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return true;
            default:
                return true;
        }
    }
}
