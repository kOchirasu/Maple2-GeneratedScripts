using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004552: Chocola
/// </summary>
public class _11004552 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 90;100;110
    }

    // Select 30:
    // $script:0116132907012728$
    // - Hey, do you need a Valentine chocolate box and some sprinkles? I've got some that I can give you. If you keep making chocolate every day, you'll get a special gift!
    protected override int Select() => 30;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (90, 0):
                // $script:0116132907012729$
                // - Hey, do you need a Valentine chocolate box and some sprinkles? I've got some that I can give you. If you keep making chocolate every day, you'll get a special gift!
                switch (selection) {
                    // $script:0116132907012730$
                    // - Give me a $item:30001287$ and $item:30001288$!
                    case 0:
                        // TODO: goto 91
                        // TODO: gotoFail 92
                        return -1;
                }
                return -1;
            case (91, 0):
                // functionID=1 openTalkReward=True 
                // $script:0116132907012731$
                // - Here you go! I hope you save some chocolate for me!
                return -1;
            case (92, 0):
                // $script:0116132907012732$
                // - Oh! Your bag is full. Try again after you make some space in your bag.
                return -1;
            case (100, 0):
                // $script:0116132907012733$
                // - The best chocolate tastes like a little nugget of love! You've still got some ingredients, so you're good to make more on your own for now. I'll give you more if you need them, of course, but keep in mind that you can only make 3 chocolates a day.
                return -1;
            case (110, 0):
                // $script:0203161007015990$
                // - $MyPCName$! Do you feel it? Love is in the air!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (90, 0) => NpcTalkButton.SelectableDistractor,
            (91, 0) => NpcTalkButton.Close,
            (92, 0) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.Close,
            (110, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
