using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004144: Iggy
/// </summary>
public class _11004144 : NpcScript {
    internal _11004144(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010559$ 
                // - Wanna split a nice glass of milk?
                return true;
            case 10:
                // $script:0806025707010560$ 
                // - Hey $male:mister,female:lady$, want to play hide-and-seek?
                return true;
            default:
                return true;
        }
    }
}
