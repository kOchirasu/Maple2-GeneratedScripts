using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003506: Seren
/// </summary>
public class _11003506 : NpcScript {
    internal _11003506(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009005$ 
                // - Do you need more candy packs?
                return true;
            case 30:
                // $script:0816160115009006$ 
                // - Ever since those hungry $itemPlural:61000002$ showed up, this place has been overflowing with tourists. I actually ran into a childhood friend the other day!
                return true;
            default:
                return true;
        }
    }
}
