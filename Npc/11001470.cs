using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001470: Gulliver Olivieta
/// </summary>
public class _11001470 : NpcScript {
    internal _11001470(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1223040807005540$ 
                // - Pass me by and you'll have a hundred years of bad luck.
                return true;
            case 30:
                // $script:1223040807005543$ 
                // - Nice place, right? If <i>you</i> lived here, you'd never have to worry about getting caught out in the rain or snow. I was going to keep it for myself, but make your best offer and this house could be yours!
                return true;
            default:
                return true;
        }
    }
}
