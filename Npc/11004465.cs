using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004465: Richmonde Guard
/// </summary>
public class _11004465 : NpcScript {
    internal _11004465(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012093$ 
                // - Who goes there? Enemy?! 
                return true;
            case 10:
                // $script:1227192907012095$ 
                // - Who goes there? Enemy?! 
                switch (selection) {
                    // $script:0111125107012684$
                    // - Hey, I'm on your side.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012096$ 
                // - Hm? Your clothes are strange, but you look like you can hold your own. You ever consider a career in freedom fighting? 
                switch (selection) {
                    // $script:1227192907012097$
                    // - Sorry, but I've got other obligations.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012098$ 
                // - Tch... What a waste of talent. Well, if you change your mind, it's not like we can afford to be picky... 
                return true;
            default:
                return true;
        }
    }
}
