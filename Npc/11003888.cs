using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003888: Celine
/// </summary>
public class _11003888 : NpcScript {
    internal _11003888(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009930$ 
                // - Listen closely to the waves. Can you hear the voice of the ocean?
                return true;
            case 20:
                // $script:0515102507009931$ 
                // - Listen closely to the waves. Can you hear the voice of the ocean?
                return true;
            case 30:
                // $script:0515102507009932$ 
                // - I'm sure you can quiet the angry seas.
                return true;
            default:
                return true;
        }
    }
}
