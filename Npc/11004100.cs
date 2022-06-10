using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004100: NPCNAME_11004100_NAME
/// </summary>
public class _11004100 : NpcScript {
    internal _11004100(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0705145607010403$ 
                // - SCRIPTNPCNAM_0705145607010403_NAME
                return true;
            case 30:
                // $script:0705145607010406$ 
                // - SCRIPTNPCNAM_0705145607010406_NAME
                switch (selection) {
                    // $script:0705145607010407$
                    // - SCRIPTNPCNAM_0705145607010407_NAME
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0705145607010408$ 
                // - SCRIPTNPCNAM_0705145607010408_NAME
                switch (selection) {
                    // $script:0705145607010409$
                    // - SCRIPTNPCNAM_0705145607010409_NAME
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0705145607010410$ 
                // - SCRIPTNPCNAM_0705145607010410_NAME
                // $script:0705145607010411$ 
                // - SCRIPTNPCNAM_0705145607010411_NAME
                switch (selection) {
                    // $script:0705145607010412$
                    // - SCRIPTNPCNAM_0705145607010412_NAME
                    case 0:
                        Id = 33;
                        return false;
                    // $script:0705145607010413$
                    // - SCRIPTNPCNAM_0705145607010413_NAME
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 33:
                // $script:0705145607010414$ 
                // - SCRIPTNPCNAM_0705145607010414_NAME
                // $script:0705145607010415$ 
                // - SCRIPTNPCNAM_0705145607010415_NAME
                return true;
            case 34:
                // $script:0705145607010416$ 
                // - SCRIPTNPCNAM_0705145607010416_NAME
                switch (selection) {
                    // $script:0705145607010417$
                    // - SCRIPTNPCNAM_0705145607010417_NAME
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0705145607010418$ 
                // - SCRIPTNPCNAM_0705145607010418_NAME
                // $script:0705145607010420$ 
                // - SCRIPTNPCNAM_0705145607010420_NAME
                return true;
            default:
                return true;
        }
    }
}
