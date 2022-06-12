using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004303: Ghost
/// </summary>
public class _11004303 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011426$
    // - This place is nice...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011429$
                // - This room's really comfy. That's why all us ghosts are here. 
                return 30;
            case (30, 1):
                // $script:1002141907011430$
                // - We don't wanna bug the living folks, though. We just wanna watch them live their lives.
                switch (selection) {
                    // $script:1002141907011431$
                    // - Did you see what happened here?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011432$
                // - I-I was scared, so I hid behind the chair! That guy was real busy. I bet he dropped a bunch of his stuff all over the place.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
