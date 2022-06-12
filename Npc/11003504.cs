using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003504: Wooji
/// </summary>
public class _11003504 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0816160115008990$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115008993$
                // - There are lots of hungry $itemPlural:61000002$ here. I'm here to capture one as a pet.
                switch (selection) {
                    // $script:0816160115008994$
                    // - Who's your little friend?
                    case 0:
                        return 31;
                    // $script:0816160115008995$
                    // - Did you come here alone?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0816160115008996$
                // - This is my $item:61000005$. We're traveling together. Say hello, $item:61000005$.
                switch (selection) {
                    // $script:0816160115008997$
                    // - Hello, Duckling.
                    case 0:
                        return 34;
                    // $script:0816160115008998$
                    // - Why are you traveling with a duckling?
                    case 1:
                        return 35;
                }
                return -1;
            case (32, 0):
                // $script:0816160115008999$
                // - No, it's just me and my $item:61000005$ on the open road! Though I did bump into my childhood friend $npcName:11003506[gender:1]$. Small world, isn't it?
                return -1;
            case (34, 0):
                // $script:0816160115009000$
                // - I guess my little $item:61000005$ is feeling shy.
                return -1;
            case (35, 0):
                // $script:0816160115009001$
                // - $item:61000005$ and I are training. I'm going to be a great pet master someday!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            (35, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
