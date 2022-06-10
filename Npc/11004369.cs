using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004369: Claus
/// </summary>
public class _11004369 : NpcScript {
    internal _11004369(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011781$ 
                // - I grow my own trees to decorate, you know. My commitment to the holidays cannot be questioned.
                return true;
            case 10:
                // $script:1109213607011782$ 
                // - My favorite memory from my childhood is decorating our tree every year. Now that I tend the garden myself, it can be even grander.
                return true;
            default:
                return true;
        }
    }
}
