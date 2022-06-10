using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000207: Arlano
/// </summary>
public class _11000207 : NpcScript {
    internal _11000207(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000889$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000891$ 
                // - Big cargo ships come through here all the time. Sometimes I think the Barrota Trading Company is more successful than Goldus.
                return true;
            default:
                return true;
        }
    }
}
