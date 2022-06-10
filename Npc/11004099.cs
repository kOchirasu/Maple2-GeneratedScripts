using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004099: NPCNAME_11004099_NAME
/// </summary>
public class _11004099 : NpcScript {
    internal _11004099(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0705145607010390$ 
                // - SCRIPTNPCNAM_0705145607010390_NAME 
                return true;
            case 30:
                // $script:0705145607010393$ 
                // - SCRIPTNPCNAM_0705145607010393_NAME 
                switch (selection) {
                    // $script:0705154107010429$
                    // - SCRIPTNPCNAM_0705154107010429_NAME
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0705154107010430$
                    // - SCRIPTNPCNAM_0705154107010430_NAME
                    case 1:
                        Id = 35;
                        return false;
                }
                return true;
            case 31:
                // $script:0705145607010397$ 
                // - SCRIPTNPCNAM_0705145607010397_NAME 
                // $script:0705145607010398$ 
                // - SCRIPTNPCNAM_0705145607010398_NAME 
                // $script:0705145607010399$ 
                // - SCRIPTNPCNAM_0705145607010399_NAME 
                return true;
            case 35:
                // $script:0705145607010400$ 
                // - SCRIPTNPCNAM_0705145607010400_NAME 
                switch (selection) {
                    // $script:0705145607010401$
                    // - SCRIPTNPCNAM_0705145607010401_NAME
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:0705145607010402$ 
                // - SCRIPTNPCNAM_0705145607010402_NAME 
                return true;
            default:
                return true;
        }
    }
}
