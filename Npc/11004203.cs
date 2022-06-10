using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004203: Tourist
/// </summary>
public class _11004203 : NpcScript {
    internal _11004203(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010654$ 
                // - It's a pleasure.
                return true;
            case 10:
                // $script:0806025707010655$ 
                // - It's a bit hot out here, but spectating is such fun!
                return true;
            default:
                return true;
        }
    }
}
