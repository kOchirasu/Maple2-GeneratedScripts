using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004552: Chocola
/// </summary>
public class _11004552 : NpcScript {
    internal _11004552(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 90;100;110
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 30:
                // $script:0116132907012728$ 
                // - Hey, do you need a Valentine chocolate box and some sprinkles? I've got some that I can give you. If you keep making chocolate every day, you'll get a special gift!
                return true;
            case 90:
                // $script:0116132907012729$ 
                // - Hey, do you need a Valentine chocolate box and some sprinkles? I've got some that I can give you. If you keep making chocolate every day, you'll get a special gift!
                switch (selection) {
                    // $script:0116132907012730$
                    // - Give me a $item:30001287$ and $item:30001288$!
                    case 0:
                        Id = 0; // TODO: 91 | 92
                        return false;
                }
                return true;
            case 91:
                // $script:0116132907012731$ functionID=1 
                // - Here you go! I hope you save some chocolate for me!
                return true;
            case 92:
                // $script:0116132907012732$ 
                // - Oh! Your bag is full. Try again after you make some space in your bag.
                return true;
            case 100:
                // $script:0116132907012733$ 
                // - The best chocolate tastes like a little nugget of love! You've still got some ingredients, so you're good to make more on your own for now. I'll give you more if you need them, of course, but keep in mind that you can only make 3 chocolates a day.
                return true;
            case 110:
                // $script:0203161007015990$ 
                // - $MyPCName$! Do you feel it? Love is in the air!
                return true;
            default:
                return true;
        }
    }
}
