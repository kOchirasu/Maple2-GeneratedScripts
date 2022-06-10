using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003415: Hero's Tomb
/// </summary>
public class _11003415 : NpcScript {
    internal _11003415(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0623153207008576$ 
                // - <i>Here lies Red Fox, courageous warrior of $map:02000051$. He laid down his life while defending our people from the forces of darkness, and for that he will always be remembered.</i>
                return true;
            case 10:
                // $script:0623180607008578$ 
                // - <i>Here lies Red Fox, courageous warrior of $map:02000051$. He laid down his life while defending our people from the forces of darkness, and for that he will always be remembered.</i>
                return true;
            default:
                return true;
        }
    }
}
