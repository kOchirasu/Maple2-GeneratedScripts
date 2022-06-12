using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003525: Rose
/// </summary>
public class _11003525 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0816160115009030$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816213215009068$
                // - We aren't open yet. Can you please come back later?
                switch (selection) {
                    // $script:0816213215009069$
                    // - Of course.
                    case 0:
                        return 32;
                    // $script:0816213215009070$
                    // - When are you opening?
                    case 1:
                        return 31;
                    // $script:0816213215009071$
                    // - Who runs this place?
                    case 2:
                        return 33;
                    // $script:0816213215009072$
                    // - What's that music?
                    case 3:
                        return 34;
                }
                return -1;
            case (31, 0):
                // $script:0816213215009073$
                // - We... don't have a date yet, actually. The boss wants to redecorate and... and hire more people.
                return -1;
            case (32, 0):
                // $script:0816213215009074$
                // - Watch your step. It's slippery over there.
                return -1;
            case (33, 0):
                // $script:0816213215009075$
                // - It seems the boss has strange tastes. He asked me to wear this outfit, even though we aren't open yet. It's so uncomfortable...
                return -1;
            case (34, 0):
                // $script:0816213215009076$
                // - Isn't it cool? It's the $map:61000008$ theme song! The boss doesn't like it, but it's pretty popular these days.
                return 34;
            case (34, 1):
                // $script:0816225215009078$
                // - Come to think of it, didn't the boss lose a game of $map:61000008$ the other day...?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
