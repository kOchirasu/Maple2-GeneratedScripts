using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000361: Marco's Secretary
/// </summary>
public class _11000361 : NpcScript {
    internal _11000361(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001499$ 
                // - How may I help you today?
                return true;
            case 30:
                // $script:0831180407001501$ 
                // - $npc:11000065[gender:0]$ is really amazing. When he sets his mind on something, nothing can stop him!
                return true;
            default:
                return true;
        }
    }
}
