using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000746: Rakael
/// </summary>
public class _11000746 : NpcScript {
    internal _11000746(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002938$ 
                // - <b>Chomp! Snarf!</b>
                return true;
            case 30:
                // $script:0831180407002941$ 
                // - Not all witches are greedy and evil. I've been studying useful spells to help $map:02000023$.
                return true;
            default:
                return true;
        }
    }
}
