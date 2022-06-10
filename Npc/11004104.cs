using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004104: NPCNAME_11004104_NAME
/// </summary>
public class _11004104 : NpcScript {
    internal _11004104(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0718090507010451$ 
                // - SCRIPTNPCNAM_0718090507010451_NAME
                return true;
            case 30:
                // $script:0718090407010434$ 
                // - SCRIPTNPCNAM_0718090407010434_NAME
                switch (selection) {
                    // $script:0718090407010435$
                    // - SCRIPTNPCNAM_0718090407010435_NAME
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0718090407010436$ 
                // - SCRIPTNPCNAM_0718090407010436_NAME
                switch (selection) {
                    // $script:0718090407010437$
                    // - SCRIPTNPCNAM_0718090407010437_NAME
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0718090407010438$ 
                // - SCRIPTNPCNAM_0718090407010438_NAME
                switch (selection) {
                    // $script:0718090407010439$
                    // - SCRIPTNPCNAM_0718090407010439_NAME
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0718090407010440$ 
                // - SCRIPTNPCNAM_0718090407010440_NAME
                return true;
            default:
                return true;
        }
    }
}
