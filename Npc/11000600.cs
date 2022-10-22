using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000600: Charles Kim
/// </summary>
public class _11000600 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 50;60;70;80;90;100;110;120;130
    }

    // Select 0:
    // $script:0831180407002402$
    // - What can I do for you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002407$
                // - You still have your $item:30000145$. Why don't you use it? You won't regret it. 
                return -1;
            case (60, 0):
                // $script:0831180407002408$
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002409$
                    // - I want another $item:30000145$.
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:0831180407002410$
                // - $MyPCName$, you already got a free $item:30000145$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002411$
                    // - Yeah, I want it.
                    case 0:
                        return 62;
                    // $script:0831180407002412$
                    // - Never mind, I don't want it.
                    case 1:
                        return 63;
                }
                return -1;
            case (62, 0):
                // $script:0831180407002413$
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002414$
                    // - Yep.
                    case 0:
                        return 65;
                    // $script:0831180407002415$
                    // - Nope.
                    case 1:
                        return 64;
                }
                return -1;
            case (63, 0):
                // $script:0831180407002416$
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000145$.
                return -1;
            case (64, 0):
                // $script:0831180407002417$
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return -1;
            case (65, 0):
                // $script:0831180407002418$
                // - Good, then it's 10,000 mesos for a $item:30000145$.
                switch (selection) {
                    // $script:0831180407002419$
                    // - Here's the money.
                    case 0:
                        // TODO: goto 66
                        // TODO: gotoFail 67
                        return 67;
                }
                return -1;
            case (66, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407002420$
                // - Here's your $item:30000145$. I hope you enjoy your new home. Bye for now!
                return -1;
            case (67, 0):
                // $script:0831180407002421$
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return -1;
            case (70, 0):
                // $script:0831180407002422$
                // - House prices have been dropping lately, attracting many potential buyers. It's kept me quite busy!
                return -1;
            case (80, 0):
                // $script:0831180407002423$
                // - You still have your $item:30000255$. Why don't you use it? You won't regret it. 
                return -1;
            case (90, 0):
                // $script:0831180407002424$
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002425$
                    // - I want another $item:30000255$.
                    case 0:
                        return 91;
                }
                return -1;
            case (91, 0):
                // $script:0831180407002426$
                // - $MyPCName$, you already got a free $item:30000255$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002427$
                    // - Yeah, I want it.
                    case 0:
                        return 92;
                    // $script:0831180407002428$
                    // - Never mind, I don't want it.
                    case 1:
                        return 93;
                }
                return -1;
            case (92, 0):
                // $script:0831180407002429$
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002430$
                    // - Yep.
                    case 0:
                        return 95;
                    // $script:0831180407002431$
                    // - Nope.
                    case 1:
                        return 94;
                }
                return -1;
            case (93, 0):
                // $script:0831180407002432$
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000255$.
                return -1;
            case (94, 0):
                // $script:0831180407002433$
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return -1;
            case (95, 0):
                // $script:0831180407002434$
                // - Good, then it's 10,000 mesos for a $item:30000255$.
                switch (selection) {
                    // $script:0831180407002435$
                    // - Here's the money.
                    case 0:
                        // TODO: goto 96
                        // TODO: gotoFail 97
                        return 97;
                }
                return -1;
            case (96, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407002436$
                // - Here's your $item:30000255$. I hope you enjoy your new home. Bye for now!
                return -1;
            case (97, 0):
                // $script:0831180407002437$
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return -1;
            case (100, 0):
                // $script:0831180407002438$
                // - You still have your $item:30000254$. Why don't you use it? You won't regret it. 
                return -1;
            case (110, 0):
                // $script:0831180407002439$
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002440$
                    // - I want another $item:30000254$.
                    case 0:
                        return 111;
                }
                return -1;
            case (111, 0):
                // $script:0831180407002441$
                // - $MyPCName$, you already got a free $item:30000254$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002442$
                    // - Yeah, I want it.
                    case 0:
                        return 112;
                    // $script:0831180407002443$
                    // - Never mind, I don't want it.
                    case 1:
                        return 113;
                }
                return -1;
            case (112, 0):
                // $script:0831180407002444$
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002445$
                    // - Yep.
                    case 0:
                        return 115;
                    // $script:0831180407002446$
                    // - Nope.
                    case 1:
                        return 114;
                }
                return -1;
            case (113, 0):
                // $script:0831180407002447$
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000254$.
                return -1;
            case (114, 0):
                // $script:0831180407002448$
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return -1;
            case (115, 0):
                // $script:0831180407002449$
                // - Good, then it's 10,000 mesos for a $item:30000254$.
                switch (selection) {
                    // $script:0831180407002450$
                    // - Here's the money.
                    case 0:
                        // TODO: goto 116
                        // TODO: gotoFail 117
                        return 117;
                }
                return -1;
            case (116, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407002451$
                // - Here's your $item:30000254$. I hope you enjoy your new home. Bye for now!
                return -1;
            case (117, 0):
                // $script:0831180407002452$
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return -1;
            case (120, 0):
                // $script:0831180407002453$
                // - You still have your $item:30000253$. Why don't you use it? You won't regret it. 
                return -1;
            case (130, 0):
                // $script:0831180407002454$
                // - Welcome, $MyPCName$! How may I help you today?
                switch (selection) {
                    // $script:0831180407002455$
                    // - I want another $item:30000253$.
                    case 0:
                        return 131;
                }
                return -1;
            case (131, 0):
                // $script:0831180407002456$
                // - $MyPCName$, you already got a free $item:30000253$ through the promotion. If you want more, then you'll have to pay 10,000 mesos each.
                switch (selection) {
                    // $script:0831180407002457$
                    // - Yeah, I want it.
                    case 0:
                        return 132;
                    // $script:0831180407002458$
                    // - Never mind, I don't want it.
                    case 1:
                        return 133;
                }
                return -1;
            case (132, 0):
                // $script:0831180407002459$
                // - Okay, just one more reminder then. If you already own a house, then you cannot buy a Maple Apartment. Makes sense, I'm sure.
                switch (selection) {
                    // $script:0831180407002460$
                    // - Yep.
                    case 0:
                        return 135;
                    // $script:0831180407002461$
                    // - Nope.
                    case 1:
                        return 134;
                }
                return -1;
            case (133, 0):
                // $script:0831180407002462$
                // - You've made the right decision. Buying a house just makes more sense financially than $item:30000253$.
                return -1;
            case (134, 0):
                // $script:0831180407002463$
                // - Oh, I'm sorry. Maple World real estate regulations restrict families to only one house. You can only buy a Maple Apartment if you don't have a house. If anything changes, feel free to come back. Bye for now!
                return -1;
            case (135, 0):
                // $script:0831180407002464$
                // - Good, then it's 10,000 mesos for a $item:30000253$.
                switch (selection) {
                    // $script:0831180407002465$
                    // - Here's the money.
                    case 0:
                        // TODO: goto 136
                        // TODO: gotoFail 137
                        return 137;
                }
                return -1;
            case (136, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407002466$
                // - Here's your $item:30000253$. I hope you enjoy your new home. Bye for now!
                return -1;
            case (137, 0):
                // $script:0831180407002467$
                // - Ah, I'm afraid the transaction didn't go through. Please make sure you have enough money and free space in your bag for the item.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.SelectableDistractor,
            (63, 0) => NpcTalkButton.Close,
            (64, 0) => NpcTalkButton.Close,
            (65, 0) => NpcTalkButton.SelectableDistractor,
            (66, 0) => NpcTalkButton.Close,
            (67, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            (80, 0) => NpcTalkButton.Close,
            (90, 0) => NpcTalkButton.SelectableDistractor,
            (91, 0) => NpcTalkButton.SelectableDistractor,
            (92, 0) => NpcTalkButton.SelectableDistractor,
            (93, 0) => NpcTalkButton.Close,
            (94, 0) => NpcTalkButton.Close,
            (95, 0) => NpcTalkButton.SelectableDistractor,
            (96, 0) => NpcTalkButton.Close,
            (97, 0) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.Close,
            (110, 0) => NpcTalkButton.SelectableDistractor,
            (111, 0) => NpcTalkButton.SelectableDistractor,
            (112, 0) => NpcTalkButton.SelectableDistractor,
            (113, 0) => NpcTalkButton.Close,
            (114, 0) => NpcTalkButton.Close,
            (115, 0) => NpcTalkButton.SelectableDistractor,
            (116, 0) => NpcTalkButton.Close,
            (117, 0) => NpcTalkButton.Close,
            (120, 0) => NpcTalkButton.Close,
            (130, 0) => NpcTalkButton.SelectableDistractor,
            (131, 0) => NpcTalkButton.SelectableDistractor,
            (132, 0) => NpcTalkButton.SelectableDistractor,
            (133, 0) => NpcTalkButton.Close,
            (134, 0) => NpcTalkButton.Close,
            (135, 0) => NpcTalkButton.SelectableDistractor,
            (136, 0) => NpcTalkButton.Close,
            (137, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
