using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000157: Paul
/// </summary>
public class _11000157 : NpcScript {
    internal _11000157(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000663$ 
                // - What seems to be the problem?
                return true;
            case 20:
                // $script:0831180407000665$ 
                // - I don't know what caused the recent earthquake. It was so strong, it tore the Royal Road in half. This could be a serious problem.
                return true;
            case 30:
                // $script:0116162507009762$ 
                // - It's really you! $MyPCName$, in the flesh!
                // $script:0116162507009763$ 
                // - It's an honor to meet you!
                switch (selection) {
                    // $script:0116162507009764$
                    // - You know me?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0116162507009765$ 
                // - You're the hero of the Siege of $map:02000001$. Of course I know you! You're a hero to all of us here.
                switch (selection) {
                    // $script:0116162507009766$
                    // - I was just doing my duty.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0116162507009767$ 
                // - You're so humble. Wow! Listen, if there's anything I can do to help you, just say the word.
                switch (selection) {
                    // $script:0116162507009768$
                    // - I'm looking into rumors about hot places. Like, super hot.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0116162507009769$ 
                // - Hot places, huh? Like unseasonably hot places?
                switch (selection) {
                    // $script:0116162507009770$
                    // - That's one example.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0116162507009771$ 
                // - Now that you mention it, I did hear a rumor from one of the merchants with the Barrota Trading Company. You heard about their new air trade routes, didn't you?
                switch (selection) {
                    // $script:0116162507009772$
                    // - I may have heard a thing or two.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0116162507009773$ 
                // - Well, a few of their routes pass over the ruins of Orbis. They say that the airships passing through the area get so hot, you can fry an egg on their decks.
                // $script:0116162507009774$ 
                // - Interesting, right?
                switch (selection) {
                    // $script:0116162507009775$
                    // - Fascinating.
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:0116170407009788$ 
                // - That's all I know.
                switch (selection) {
                    // $script:0116170407009789$
                    // - It was a big help.
                    case 0:
                        Id = 37;
                        return false;
                }
                return true;
            case 37:
                // $script:0116162507009776$ 
                // - I can't believe <i>I</i> am getting to talk to <i>you</i> about real important official business! Don't worry, $male:sir,female:ma'am$, I'll do my best to keep $map:02000001$ safe, too!
                return true;
            default:
                return true;
        }
    }
}
