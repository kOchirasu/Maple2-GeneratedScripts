using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000482: Puzroon's Message
/// </summary>
public class _11000482 : NpcScript {
    internal _11000482(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002109$ 
                // - Judging by the rough handwriting, I think $npcName:11000441[gender:0]$ wrote this note.
                return true;
            case 10:
                // $script:0831180407002110$ 
                // - Judging by the rough handwriting, I think $npcName:11000441[gender:0]$ wrote this note.
                switch (selection) {
                    // $script:0831180407002111$
                    // - Check the note about the starting time.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180407002112$
                    // - Check the note about how to play the game.
                    case 1:
                        Id = 12;
                        return false;
                    // $script:0831180407002113$
                    // - Check the note about earning rewards.
                    case 2:
                        Id = 13;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180407002114$ 
                // - I know these folks aren't just here to see $npcName:11000441[gender:0]$. Don't worry, I'll start the game when we've got enough people.
                return true;
            case 12:
                // $script:0831180407002115$ 
                // - Step on the red tile to jump to the center of the cave. Once there, you can step on the blue tile there when you want to leave.
                // $script:0831180407002116$ 
                // - When the game begins, the tiles you're standing on will start disappearing. Last as long as you can without falling, and if you're the last one standing, you win! Easy, right?
                return true;
            case 13:
                // $script:0831180407002117$ 
                // - In addition to mesos, the winners will get a special reward: $npcName:11000441[gender:0]$'s Blessing, which increases their Movement Speed for 15 seconds.
                // $script:0831180407002118$ 
                // - Do you want a reward? Then join up and complete the game!
                return true;
            default:
                return true;
        }
    }
}
