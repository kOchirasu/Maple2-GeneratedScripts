using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001692: Hub Computer
/// </summary>
public class _11001692 : NpcScript {
    internal _11001692(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 5;10;11;12;13;14;15;20;30;40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006502$ 
                // - Connecting to the BeyondLink database...
                return true;
            case 5:
                // $script:0728011907006927$ 
                // - Connecting to the BeyondLink database... Error: Invalid credentials.
                return true;
            case 10:
                // $script:0629000607006503$ 
                // - Connecting to the BeyondLink database... Connection established.
                switch (selection) {
                    // $script:0705132707006621$
                    // - (View Code 0.)
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0705132707006622$ 
                // - Code 0
                //   Project Hand: Summoning System/Transdimensional Implementation
                switch (selection) {
                    // $script:0705132707006623$
                    // - (View Code 1.)
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0705132707006624$ 
                // - Code 1
                //   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
                switch (selection) {
                    // $script:0705132707006625$
                    // - (Next page.)
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0705132707006626$ 
                // - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
                switch (selection) {
                    // $script:0705132707006627$
                    // - (View Code 2.)
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:0705132707006628$ 
                // - Code 2
                //   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
                switch (selection) {
                    // $script:0705132707006629$
                    // - (Next page.)
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:0705132707006630$ 
                // - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
                return true;
            case 20:
                // $script:0728011907006928$ 
                // - Confirming connection to BeyondLink... Please scan your iris to verify your credentials.
                return true;
            case 30:
                // $script:0728011907006929$ 
                // - You must first verify your credentials before accessing files. You may only access files for which your account has access permission.
                return true;
            case 40:
                // $script:0728011907006947$ 
                // - <font color="#ffd200">Confirm Target: Lost Child</font>
                switch (selection) {
                    // $script:0805105407007103$
                    // - <font color="#909090">(Your vision blurs and you feel dizzy.)</font>
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0804163407007059$ functionID=1 
                // - System Command: Absorb target's energy.
                return true;
            case 50:
                // $script:0805105407007104$ 
                // - Connecting to the BeyondLink database... Connection established.
                switch (selection) {
                    // $script:0805105407007105$
                    // - (View Code 0.)
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0805105407007106$ 
                // - Code 0
                //   Project Hand: Summoning System/Transdimensional Implementation
                switch (selection) {
                    // $script:0805105407007107$
                    // - (View Code 1.)
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:0805105407007108$ 
                // - Code 1
                //   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
                switch (selection) {
                    // $script:0805105407007109$
                    // - (Next page.)
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:0805105407007110$ 
                // - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
                switch (selection) {
                    // $script:0805105407007111$
                    // - (View Code 2.)
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            case 54:
                // $script:0805105407007112$ 
                // - Code 2
                //   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
                switch (selection) {
                    // $script:0805105407007113$
                    // - (Next page.)
                    case 0:
                        Id = 55;
                        return false;
                }
                return true;
            case 55:
                // $script:0805105407007114$ 
                // - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
                return true;
            case 60:
                // $script:0805105407007115$ 
                // - Connecting to the BeyondLink database... Connection established.
                switch (selection) {
                    // $script:0805105407007116$
                    // - (View Code 0.)
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:0805105407007117$ 
                // - Code 0
                //   Project Hand: Summoning System/Transdimensional Implementation
                switch (selection) {
                    // $script:0805105407007118$
                    // - (View Code 1.)
                    case 0:
                        Id = 62;
                        return false;
                }
                return true;
            case 62:
                // $script:0805105407007119$ 
                // - Code 1
                //   Project Mantra: Narubashan purification rate is normal. Mental and physical changes detected during administration.
                switch (selection) {
                    // $script:0805105407007120$
                    // - (Next page.)
                    case 0:
                        Id = 63;
                        return false;
                }
                return true;
            case 63:
                // $script:0805105407007121$ 
                // - More sample data is required. Out of 100 personnel supplied by Katramus through the Red Cape, only half can move on to phase 2. Conversion to phase 3 requires the restoration of the missing prototype.
                switch (selection) {
                    // $script:0805105407007122$
                    // - (View Code 2.)
                    case 0:
                        Id = 64;
                        return false;
                }
                return true;
            case 64:
                // $script:0805105407007123$ 
                // - Code 2
                //   Project Katramus: Linking $map:03000145$ data not necessary. Code 1 is the highest priority.
                switch (selection) {
                    // $script:0805105407007124$
                    // - (Next page.)
                    case 0:
                        Id = 65;
                        return false;
                }
                return true;
            case 65:
                // $script:0805105407007125$ 
                // - Code 1 Support Proposal: Move Dr. Rokel's project. Given current situation, highly likely that Code 2 will be terminated.
                return true;
            default:
                return true;
        }
    }
}
