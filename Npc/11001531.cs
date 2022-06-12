using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001531: Cantata
/// </summary>
public class _11001531 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0318211907005959$
    // - Dance and play! It's not hard if you're having fun.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0318211907005963$
                // - Dance and play! It's not hard if you're having fun.
                switch (selection) {
                    // $script:0318211907005964$
                    // - How do you play Dance, Dance, Stop?
                    case 0:
                        return 41;
                    // $script:0318211907005965$
                    // - I got eliminated. It's not fair!
                    case 1:
                        return 47;
                    // $script:0318211907005966$
                    // - What are you doing here?
                    case 2:
                        return 48;
                }
                return -1;
            case (41, 0):
                // $script:0318211907005967$
                // - When the numbers appear on the floor panels, hop on them! If you match the number of dancers to the number, you go on to the next round. Otherwise... you're out!
                switch (selection) {
                    // $script:0318211907005968$
                    // - How do you win? 
                    case 0:
                        return 42;
                    // $script:0318211907005969$
                    // - I don't know how to dance.
                    case 1:
                        return 46;
                }
                return -1;
            case (42, 0):
                // $script:0318211907005970$
                // - Last 5 rounds, and you win. But the longer the game goes on, the less time you have to get on a panel. If you're a quick thinker and a fast runner, you can win... even if you're a terrible dancer!
                switch (selection) {
                    // $script:0318211907005971$
                    // - Do you have any tips?
                    case 0:
                        return 43;
                    // $script:0318211907005972$
                    // - I'll win next time!
                    case 1:
                        return 45;
                }
                return -1;
            case (43, 0):
                // $script:0318211907005973$
                // - You know I do! Dancing isn't just fun—it's a great way to get experience. Once you're on a tile for 2 or more dancers, you can block others from joining you. This is a great way to lock down a tricky number and get a fabulous bonus.
                return 43;
            case (43, 1):
                // $script:0318211907005974$
                // - Just press the action key to block others from joining your panel. You can't leave the tile while you're doing this, so when you're done be sure to press the action key again. But the most important tip I have... is to <i>have fun!</i>
                switch (selection) {
                    // $script:0318211907005975$
                    // - I'll win next time!
                    case 0:
                        return 45;
                }
                return -1;
            case (45, 0):
                // $script:0318211907005976$
                // - That's the spirit! Keep it real, my friend. Keep it real.
                return -1;
            case (46, 0):
                // $script:0318211907005977$
                // - Don't even sweat it. Just press the yellow light on the floor, and <i>bam!</i> It's dance time! Press the action key to boogie down with some random dance moves.
                switch (selection) {
                    // $script:0318211907005978$
                    // - How do you win? 
                    case 0:
                        return 42;
                    // $script:0318211907005979$
                    // - I'll win next time!
                    case 1:
                        return 45;
                }
                return -1;
            case (47, 0):
                // $script:0318211907005980$
                // - Don't let it get to you, my downtrodden dancer. Even if you're eliminated, there's a special dance floor where you can strut yourself. Just go to the yellow stage and press the action key!
                switch (selection) {
                    // $script:0318211907005981$
                    // - What's the secret to winning the game?
                    case 0:
                        return 42;
                    // $script:0318211907005982$
                    // - I'll win next time!
                    case 1:
                        return 45;
                }
                return -1;
            case (48, 0):
                // $script:0318211907005983$
                // - The best way to know how someone really feels is to watch him dance. I learn so much about human emotion by studying the dancers here. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Next,
            (43, 1) => NpcTalkButton.SelectableDistractor,
            (45, 0) => NpcTalkButton.Close,
            (46, 0) => NpcTalkButton.SelectableDistractor,
            (47, 0) => NpcTalkButton.SelectableDistractor,
            (48, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
