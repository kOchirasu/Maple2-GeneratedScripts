using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001408: Dali
/// </summary>
public class _11001408 : NpcScript {
    internal _11001408(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005405$ 
                // - Welcome to <i>our</i> territory, human. 
                return true;
            case 40:
                // $script:1222203907005480$ 
                // - We don't usually let our clients in here. Seeing us train and tend to our wounded makes them realize that we, too, are mortal. It's bad for the brand, see?
                // $script:1222203907005481$ 
                // - We like humans, of course, but we know better than to count them as friends. We once relied on our humans for happiness. That... didn't end well for us.
                // $script:1222203907005482$ 
                // - Anyway, now that you've seen our base, you have to promise never to tell anyone about it. Only you and your closest friends are welcome here.
                return true;
            default:
                return true;
        }
    }
}
