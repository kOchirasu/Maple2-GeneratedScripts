using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003436: Jorge
/// </summary>
public class _11003436 : NpcScript {
    internal _11003436(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008684$ 
                // - It's a tad noisy here for my tastes.
                return true;
            case 10:
                // $script:0721142007008702$ 
                // - It's a tad noisy here for my tastes.
                return true;
            default:
                return true;
        }
    }
}
