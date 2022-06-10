using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004105: NPCNAME_11004105_NAME
/// </summary>
public class _11004105 : NpcScript {
    internal _11004105(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0718090507010452$ 
                // - SCRIPTNPCNAM_0718090507010452_NAME 
                return true;
            case 30:
                // $script:0718090407010444$ 
                // - SCRIPTNPCNAM_0718090407010444_NAME 
                switch (selection) {
                    // $script:0718090407010445$
                    // - SCRIPTNPCNAM_0718090407010445_NAME
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0718090407010446$ 
                // - SCRIPTNPCNAM_0718090407010446_NAME 
                switch (selection) {
                    // $script:0718090407010447$
                    // - SCRIPTNPCNAM_0718090407010447_NAME
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0718090407010448$ 
                // - SCRIPTNPCNAM_0718090407010448_NAME 
                // $script:0718090407010449$ 
                // - SCRIPTNPCNAM_0718090407010449_NAME 
                // $script:0718090407010450$ 
                // - SCRIPTNPCNAM_0718090407010450_NAME 
                return true;
            default:
                return true;
        }
    }
}
