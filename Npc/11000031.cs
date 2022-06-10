using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000031: Asimov
/// </summary>
public class _11000031 : NpcScript {
    internal _11000031(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000181$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0831180407000182$ 
                // - The power of the Green Lapenta is especially strong here in $map:02000023$. That vital force protects this place from darkness.
                return true;
            default:
                return true;
        }
    }
}
