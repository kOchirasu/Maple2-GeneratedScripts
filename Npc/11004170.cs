using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004170: Mika
/// </summary>
public class _11004170 : NpcScript {
    internal _11004170(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010597$ 
                // - What is it? 
                return true;
            case 10:
                // $script:0806025707010598$ 
                // - It's been too long since we've been together like this. Time to warm up! 
                return true;
            default:
                return true;
        }
    }
}
