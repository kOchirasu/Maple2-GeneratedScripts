using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003526: Rain
/// </summary>
public class _11003526 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0816160115009037$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009038$
                // - Sh. I'm trying to think of a melody. Can you give me a minute?
                switch (selection) {
                    // $script:0816160115009039$
                    // - Yeah, goodbye.
                    case 0:
                        return 36;
                    // $script:0816160115009040$
                    // - (Wait.)
                    case 1:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0816160115009041$
                // - ♬ Compelled to capture every pet! You and I, together! ♬
                switch (selection) {
                    // $script:0816160115009042$
                    // - Yeah, goodbye.
                    case 0:
                        return 36;
                    // $script:0816160115009043$
                    // - (Wait a little more.)
                    case 1:
                        return 32;
                }
                return -1;
            case (36, 0):
                // $script:0816170815009057$
                // - ♬ I wish for unparalleled skill... ♬
                return -1;
            case (32, 0):
                // $script:0816160115009044$
                // - A fan, are you? Want my autograph? An advanced copy of my album? Well, it's coming out soon, so you'll just have to wait!
                switch (selection) {
                    // $script:0816160115009045$
                    // - I'd like to hear a song.
                    case 0:
                        return 33;
                    // $script:0816160115009046$
                    // - I want to know about your pet.
                    case 1:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:0816160115009047$
                // - My new song is a secret! You'll have to wait for the single, like everybody else.
                return -1;
            case (34, 0):
                // $script:0816160115009048$
                // - This one... this one cannot be tamed. It's special.
                switch (selection) {
                    // $script:0816160115009049$
                    // - Where can I get one?
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:0816160115009050$
                // - That's my secret!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
