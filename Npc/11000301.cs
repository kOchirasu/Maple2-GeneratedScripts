using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000301: Jax
/// </summary>
public class _11000301 : NpcScript {
    internal _11000301(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001194$ 
                // - What brings you? 
                return true;
            case 20:
                // $script:0831180407001196$ 
                // - This place is dangerous. Be careful, especially if you want to use skills while on the Bone Bridge. Things can get scary there pretty quickly. 
                return true;
            default:
                return true;
        }
    }
}
