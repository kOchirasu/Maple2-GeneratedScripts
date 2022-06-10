using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000541: Tai
/// </summary>
public class _11000541 : NpcScript {
    internal _11000541(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002307$ 
                // - What's wrong? 
                return true;
            case 20:
                // $script:0831180407002309$ 
                // - The worst thing that can happen to anyone is losing their home. It's like having the ground ripped out from under you. 
                return true;
            case 30:
                // $script:0831180407002310$ 
                // - An eye for an eye... I'm going to teach them what it feels like to have your life shaken to its roots. 
                return true;
            default:
                return true;
        }
    }
}
