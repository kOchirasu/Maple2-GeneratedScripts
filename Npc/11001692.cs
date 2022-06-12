using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001692: Hub Computer
/// </summary>
public class _11001692 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 5;10;11;12;13;14;15;20;30;40;50;60
    }

    // Select 0:
    // $script:0629000607006502$
    // - Connecting to the BeyondLink database...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (5, 0):
                // $script:0728011907006927$
                // - Connecting to the BeyondLink database... Error: Invalid credentials.
                return -1;
            case (10, 0):
                // $script:0629000607006503$
                // - Connecting to the BeyondLink database... Connection established.
                switch (selection) {
                    // $script:0705132707006621$
                    // - (View Code 0.)
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0705132707006622$
                // - Code 0
                //   Project Hand: Summoning System/Transdimensional Implementation
                switch (selection) {
                    // $script:0705132707006623$
                    // - (View Code 1.)
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0705132707006624$
                // - Code 1
                //   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
                switch (selection) {
                    // $script:0705132707006625$
                    // - (Next page.)
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0705132707006626$
                // - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
                switch (selection) {
                    // $script:0705132707006627$
                    // - (View Code 2.)
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:0705132707006628$
                // - Code 2
                //   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
                switch (selection) {
                    // $script:0705132707006629$
                    // - (Next page.)
                    case 0:
                        return 15;
                }
                return -1;
            case (15, 0):
                // $script:0705132707006630$
                // - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
                return -1;
            case (20, 0):
                // $script:0728011907006928$
                // - Confirming connection to BeyondLink... Please scan your iris to verify your credentials.
                return -1;
            case (30, 0):
                // $script:0728011907006929$
                // - You must first verify your credentials before accessing files. You may only access files for which your account has access permission.
                return -1;
            case (40, 0):
                // $script:0728011907006947$
                // - <font color="#ffd200">Confirm Target: Lost Child</font>
                switch (selection) {
                    // $script:0805105407007103$
                    // - <font color="#909090">(Your vision blurs and you feel dizzy.)</font>
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // functionID=1 
                // $script:0804163407007059$
                // - System Command: Absorb target's energy.
                return -1;
            case (50, 0):
                // $script:0805105407007104$
                // - Connecting to the BeyondLink database... Connection established.
                switch (selection) {
                    // $script:0805105407007105$
                    // - (View Code 0.)
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0805105407007106$
                // - Code 0
                //   Project Hand: Summoning System/Transdimensional Implementation
                switch (selection) {
                    // $script:0805105407007107$
                    // - (View Code 1.)
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:0805105407007108$
                // - Code 1
                //   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
                switch (selection) {
                    // $script:0805105407007109$
                    // - (Next page.)
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:0805105407007110$
                // - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
                switch (selection) {
                    // $script:0805105407007111$
                    // - (View Code 2.)
                    case 0:
                        return 54;
                }
                return -1;
            case (54, 0):
                // $script:0805105407007112$
                // - Code 2
                //   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
                switch (selection) {
                    // $script:0805105407007113$
                    // - (Next page.)
                    case 0:
                        return 55;
                }
                return -1;
            case (55, 0):
                // $script:0805105407007114$
                // - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
                return -1;
            case (60, 0):
                // $script:0805105407007115$
                // - Connecting to the BeyondLink database... Connection established.
                switch (selection) {
                    // $script:0805105407007116$
                    // - (View Code 0.)
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:0805105407007117$
                // - Code 0
                //   Project Hand: Summoning System/Transdimensional Implementation
                switch (selection) {
                    // $script:0805105407007118$
                    // - (View Code 1.)
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:0805105407007119$
                // - Code 1
                //   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
                switch (selection) {
                    // $script:0805105407007120$
                    // - (Next page.)
                    case 0:
                        return 63;
                }
                return -1;
            case (63, 0):
                // $script:0805105407007121$
                // - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
                switch (selection) {
                    // $script:0805105407007122$
                    // - (View Code 2.)
                    case 0:
                        return 64;
                }
                return -1;
            case (64, 0):
                // $script:0805105407007123$
                // - Code 2
                //   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
                switch (selection) {
                    // $script:0805105407007124$
                    // - (Next page.)
                    case 0:
                        return 65;
                }
                return -1;
            case (65, 0):
                // $script:0805105407007125$
                // - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (5, 0) => NpcTalkButton.Close,
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.SelectableDistractor,
            (54, 0) => NpcTalkButton.SelectableDistractor,
            (55, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.SelectableDistractor,
            (63, 0) => NpcTalkButton.SelectableDistractor,
            (64, 0) => NpcTalkButton.SelectableDistractor,
            (65, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
